from django.shortcuts import render
from .models import Book, BooksCategory, BooksMaincategory, BooksSubcategory  #models에 테이블 관련 class 가져오기?
from .models import Review
from django import forms
from django.views import generic  #django에 있는 기본 view로 테스트
from django.views.generic.edit import FormView
from django.db.models import Q
from django.utils import timezone
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from .serializers import BookSerializer, ReviewSerializer, SubCategorySerializer, MainCategorySerializer
from rest_framework import status
from rest_framework.decorators import api_view
from accounts.models import Dibs


@api_view(('GET', ))
def booklist(request):  #얘 request 필요해 . . .?
    book_list = Book.objects.all()  #BooksBook 테이블의 모든 정보 가져오기
    serializer = BookSerializer(book_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 모든 책을 가져오고나서 .. .. 검색인데 ㅇㅁㅇ
#미완성!
def search(request):
    books = Book.objects.all().order_by('-book_id')
    contents = request.POST.get('contents', "")

    if contents:
        books = books.filter(
            Q(book_title__icontains=contents)
            | Q(book_author__icontains=contents)).distinct()
        # | Q(book_subcategory__icontains=contents)).distinct()
        #Q객체 : filter()메소드의 조건을 다양하게 줄 수 있음
        #icontains 연산자 : 대소문자를 구분하지 않고 단어가 포함되어있는지 검사
        #distinct() : 중복된 객체 제외

        return render(request, 'search_book.html', {
            'books': books,
            'contents': contents
        })

    else:
        return render(request, 'search_book.html')


#도서 상세 정보
@api_view(('POST', ))
def detail(request, book_id):
    user_id = request.data['user_id']
    book = Book.objects.get(book_id=book_id)
    serializer = BookSerializer(book)
    # context = {
    #     'book': book,
    # }
    #리뷰 작성했는지 확인하는 sql 필요
    #여기서 리뷰를 작성한 사람이면 "리뷰작성함" 메시지를 보내야하고
    isWritten = Review.objects.filter(Q(book_id=book_id) & Q(user_id=user_id))
    myreview = []
    if isWritten:
        myreview = list(isWritten.values())[0]  #화면에 띄워주기 편하려고!
    #리뷰를 작성하지 않은 사람이면 "리뷰작성안함" 메시지를 보내서 리뷰작성 버튼을 만들어야지
    else:
        myreview = []

    #찜했는지 여부도 같이 보내야함!
    dibSelected = list(
        Dibs.objects.filter(Q(book_id=book_id) & Q(user_id=user_id)).values())
    dibSelectYes = False
    if dibSelected[0]['is_selected']:  #찜했으면 True 보내주기!
        dibSelectYes = True

    #여기에 category도 보내줘야댐!!!!
    #1. book_isbn을 찾기
    book_isbn = serializer.data['book_isbn']

    #2. book.book_isbn = book_category.book_id 인 main_category랑 sub_category 찾기
    categoryData = BooksCategory.objects.get(book_id=book_isbn)

    main_category_id = categoryData.main_category
    sub_category_id = categoryData.sub_category

    #3. main_category 테이블에서 main_category이름과, sub_category 테이블에서 sub_category이름을 찾아서 넘기기
    main_category_name = BooksMaincategory.objects.get(
        id=main_category_id).name

    sub_category_name = BooksSubcategory.objects.get(id=sub_category_id).name

    return Response(
        {
            "book": serializer.data,  #책세부내용
            "maincategory": main_category_name,  #카테고리 - 메인
            "subcategory": sub_category_name,  #카테고리 - 서브
            "myreview": myreview,  #리뷰달았는지 yes(리뷰내용) no(빈리스트)
            "mydibs": dibSelectYes,  #찜했는지 yes(True) no(False)
        },
        status=status.HTTP_200_OK)


#메인 카테고리들 전송
@api_view(["POST"])
def maincategory(request):
    #main_category table에 있는 모든 정보 전송
    categories = BooksMaincategory.objects.all()
    serializer = MainCategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


#메인 카테고리에 따른 서브 카테고리 목록 전송
@api_view(["POST"])
def subcategory(request, main_id):
    #sub_category에서 main = 받아온 main_id 인 sub_category의 id와 name 전달
    categories = BooksSubcategory.objects.filter(Q(main=main_id))
    serializer = SubCategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


#서브 카테고리 별 도서 목록 전송 -> 메인카테고리/서브카테고리도 같이 보내기
#서브 카테고리를 선택하지 않을 수도 있음 : sub_id를 1로 설정해두자(front에서)
@api_view(["POST"])
def categorybooks(request):
    main_id = request.data['main_id']
    sub_id = request.data['sub_id']
    #main_id가 0인지 아닌지
    if main_id == 0:
        ####도서 전체 목록!!!! + 그 도서의 카테고리...이름까지 같이 넘어와야 할 듯
        print("")

    else:
        #sub_id가 1인지 아닌지
        if sub_id == 1:
            #메인카테고리에 따른 도서 목록 가져오기
            #1. books_category에서 해당 main_category가 같은 book_id를 추출해서
            #2. books_book에서 book_isbn과 같은 도서 목록을 추출
            #3. 이 때, sub_category의 이름도 같이 보내기
            print("")

        else:
            #서브카테고리에 따른 도서 목록 가져오기
            print("")

    return Response(status=status.HTTP_200_OK)


#리뷰 작성
@api_view(["POST"])
def createReview(request):
    # print("request")
    # print(request.data)
    new_review = ReviewSerializer(data=request.data)
    if not new_review.is_valid(raise_exception=True):
        return Response({'message': 'Request Body Error'},
                        status=status.HTTP_409_CONFLICT)

    new_review.is_valid(raise_exception=True)  # 파라미터 : 유효성 검사, 실패시 예외 발생
    new_review.save()

    return Response(status=status.HTTP_200_OK)  #그냥 성공했다 이거만 보내면 되겠지?


#리뷰 수정
@api_view(["POST"])
def updateReview(request, review_id):
    #review_id에 해당하는 내용을 찾아서 instance에 삽입 후
    instance = Review.objects.get(review_id=review_id)

    #vue.js에서 넘어온 데이터를 new_review에 넣고
    new_review = ReviewSerializer(data=request.data)

    #유효성 검사를 하고
    if not new_review.is_valid(raise_exception=True):
        return Response({'message': 'Request Body Error'},
                        status=status.HTTP_409_CONFLICT)

    new_review.is_valid(raise_exception=True)  # 파라미터 : 유효성 검사, 실패시 예외 발생

    #리뷰 평점, 리뷰 내용, 리뷰 수정날짜를 바꿔줌!! : 이 때 user_id랑 book_id는 바꿀 필요가 없으므로 쓰지 않는걸로...
    instance.review_rating = new_review.data['review_rating']
    instance.review_content = new_review.data['review_content']
    instance.review_date = timezone.now()
    instance.save()
    return Response(status=status.HTTP_200_OK)  #그냥 성공했다 이거만 보내면 되겠지?


#리뷰 삭제
@api_view(["DELETE"])
def deleteReview(request, review_id):
    post_instance = Review.objects.get(review_id=review_id)
    post_instance.delete()
    return Response(status=status.HTTP_200_OK)  #그냥 성공했다 이거만 보내면 되겠지?