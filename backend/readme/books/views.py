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
from .serializers import BookSerializer, ReviewSerializer, SubCategorySerializer, MainCategorySerializer,\
                        CategoryQuerySerializer, BookSearchQuerySerializer
from rest_framework import status
from rest_framework.decorators import api_view
from accounts.models import Dibs
from .pagination import ListPageNumberPagination
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


@api_view(('GET', ))
def booklist(request):  #얘 request 필요해 . . .?
    book_list = Book.objects.all()  #BooksBook 테이블의 모든 정보 가져오기
    serializer = BookSerializer(book_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 책 검색 API
@swagger_auto_schema(method='get', query_serializer=BookSearchQuerySerializer)
@api_view(('GET', ))
def search(request):
    keyword = request.GET.get('keyword', '')
    search_type = request.GET.get('search_type', 'all')
    print(search_type)
    # contents = request.POST.get('contents', "")
    book_list = Book.objects.order_by('-book_id')
    # 페이징 처리
    paginator = ListPageNumberPagination()

    if keyword:
        # | Q(book_subcategory__icontains=contents)).distinct()
        #Q객체 : filter()메소드의 조건을 다양하게 줄 수 있음
        #icontains 연산자 : 대소문자를 구분하지 않고 단어가 포함되어있는지 검사
        #distinct() : 중복된 객체 제외
        if search_type == 'all':
            search_book_list = book_list.filter(Q(book_title__icontains=keyword)
                                                 | Q(book_author__icontains=keyword)
                                                 | Q(book_description__icontains=keyword))
        elif search_type == 'title':
            search_book_list = book_list.filter(book_title__icontains=keyword)
        elif search_type == 'author':
            search_book_list = book_list.filter(book_author__icontains=keyword)
        else:
            search_book_list = book_list.filter(book_description__icontains=keyword)
        
        book_list = search_book_list

    count = book_list.count()

    book_list = paginator.paginate_queryset(book_list, request)
    serializer = BookSerializer(book_list, many=True)

    return Response({
        "books": serializer.data,
        "total_count": count,
    }, status = status.HTTP_200_OK)


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

# category_search를 위한 query parameter
# main_id_param = openapi.Parameter('main_id', openapi.IN_QUERY, description="주 카테고리의 id", type=openapi.TYPE_INTEGER)
# sub_id_param = openapi.Parameter('sub_id', openapi.IN_QUERY, description="서브 카테고리의 id", type=openapi.TYPE_INTEGER)

#서브 카테고리 별 도서 목록 전송 -> 메인카테고리/서브카테고리도 같이 보내기
#서브 카테고리를 선택하지 않을 수도 있음 : sub_id를 1로 설정해두자(front에서)
@swagger_auto_schema(method='get', query_serializer=CategoryQuerySerializer)
# @swagger_auto_schema(method='get', manual_parameters=[main_id_param, sub_id_param])
@api_view(("GET", ))
def category_search(request):
    main_id = request.GET.get('main_id', '')
    sub_id = request.GET.get('sub_id', '')
    main_category_name = ''
    sub_category_name = ''
    if main_id:
        main_category_name = BooksMaincategory.objects.get(id=main_id).name
    if sub_id:
        sub_category_name = BooksSubcategory.objects.get(id=sub_id).name
    
    ####도서 전체 목록!!!! + 그 도서의 카테고리...이름까지 같이 넘어와야 할 듯
    book_category_list = BooksCategory.objects.all()  #BooksCategory 테이블의 모든 정보 가져오기

    #main_id가 0인지 아닌지 : 사용자가 main_category를 선택했는지 안했는지
    if main_id and main_id != 0:
        #메인카테고리에 따른 도서 목록 가져오기
        #1. books_category에서 해당 main_category가 같은 book_id를 추출해서
        #2. books_book에서 book_isbn과 같은 도서 목록을 추출
        #3. 이 때, sub_category의 이름도 같이 보내기
        book_category_list = book_category_list.filter(main_category = main_id)

        #sub_id가 1인지 아닌지 : 사용자가 sub_category를 선택했는지 안했는지
        if sub_id and sub_id != 1:
            book_category_list = book_category_list.filter(sub_category = sub_id)

    # book_category_list 에서 book_id의 필드값만 뽑아와 리스트로 반환
    # print(list(book_category_list.values_list('book_id', flat=True)))
    book_list = Book.objects.filter(book_isbn__in = list(book_category_list.values_list('book_id', flat=True)))
    count = book_list.count()
    # print(book_list)

    # 페이징 처리를 위해 만들어놓은 ListPageNumberPagination 클래스를 이용
    paginator = ListPageNumberPagination()
    book_list = paginator.paginate_queryset(book_list, request)

    serializer = BookSerializer(book_list, many=True)

    return Response({
            "books": serializer.data,
            "maincategory": main_category_name,  #카테고리 - 메인
            "subcategory": sub_category_name,  #카테고리 - 서브
            "total_count": count,
        }, status=status.HTTP_200_OK)


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