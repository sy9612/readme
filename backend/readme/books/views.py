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
                        CategoryQuerySerializer, BookSearchQuerySerializer, BookDetailSerializer, UserIdSerializer, UserReviewSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from accounts.models import Dibs
from .pagination import ListPageNumberPagination
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


page_param = openapi.Parameter('page', openapi.IN_QUERY, description="페이지 넘버(한 페이지당 25개의 결과)", type=openapi.TYPE_INTEGER)

@swagger_auto_schema(method='get', manual_parameters=[page_param])
@api_view(('GET', ))
def book_list(request):
    '''
        전체 책 리스트 반환

        ---
    '''
    book_list = Book.objects.all()  #BooksBook 테이블의 모든 정보 가져오기
    # 페이징 처리
    paginator = ListPageNumberPagination()
    book_list = paginator.paginate_queryset(book_list, request)
    serializer = BookSerializer(book_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# 책 검색 API
@swagger_auto_schema(method='get', query_serializer=BookSearchQuerySerializer)
@api_view(('GET', ))
def search(request):
    '''
        type과 keyword에 해당하는 책 정보 검색

        --- 
    '''
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
@swagger_auto_schema(method='post', request_body=UserIdSerializer)
@api_view(('POST', ))
def detail(request, book_isbn):
    '''
        도서 상세 정보를 반환

        ---
        # Response(카테고리 정보가 있는 경우)
            - book : 책정보, 평균별점, 리뷰개수
            - maincategory : 메인카테고리 이름 (리스트)
            - subcategory : 서브카테고리 이름  (리스트)
            - is_dibs : 찜 여부
        
        # Response(카테고리 정보가 없는 경우)
            - book : 책정보, 평균별점, 리뷰개수
            - is_dibs : 찜 여부
    '''
    user_id = request.data['user_id']

    book = Book.objects.get(book_isbn=book_isbn)
    serializer = BookDetailSerializer(book)
    
    try:
        dibs = Dibs.objects.get(Q(book_isbn=book_isbn) & Q(user_id=user_id))
        is_selected = dibs.is_selected
    except Dibs.DoesNotExist:
        is_selected = 0

    #2. book.book_isbn = book_category.book_id 인 main_category랑 sub_category 찾기
    categoryData = BooksCategory.objects.filter(book_isbn=book_isbn)
    if len(categoryData) != 0:
        #3. main_category 테이블에서 main_category이름과, sub_category 테이블에서 sub_category이름을 찾아서 넘기기
        main_category_name = BooksMaincategory.objects.filter(
            id__in=categoryData.values_list('main_category', flat=True)).values_list('name', flat=True)

        sub_category_name = BooksSubcategory.objects.filter(
            id__in=categoryData.values_list('sub_category', flat=True)).values_list('name', flat=True)

        return Response(
            {
                "book": serializer.data,  #책세부내용
                "maincategory": main_category_name,  #카테고리 - 메인
                "subcategory": sub_category_name,  #카테고리 - 서브
                "is_dibs" : is_selected,
            },
            status=status.HTTP_200_OK)
    else:
         return Response(
            {
                "book": serializer.data,  #책세부내용
                "is_dibs" : is_selected,
            }, status = status.HTTP_200_OK)


#메인 카테고리들 전송
@api_view(["POST"])
def maincategory(request):
    '''
        메인 카테고리 리스트 전송

        ---
    '''
    #main_category table에 있는 모든 정보 전송
    categories = BooksMaincategory.objects.all()
    serializer = MainCategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


#메인 카테고리에 따른 서브 카테고리 목록 전송
@api_view(["POST"])
def subcategory(request, main_id):
    '''
        메인 카테고리에 따른 서브 카테고리 리스트 전송

        ---
    '''
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
    '''
        메인 카테고리, 서브 카테고리의 id를 입력받아 해당되는 책 리스트 반환

        ---
        # Response
            - book          : 책 정보 data
            - maincategory  : 메인 카테고리 이름
            - subcategory   : 서브 카테고리 이름
            - total_count   : 검색 결과 수
    '''
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
    book_list = Book.objects.filter(book_isbn__in = list(book_category_list.values_list('book_isbn', flat=True)))
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


# 리뷰 리스트 API
@api_view(("GET", "POST",))
def review_list(request, book_isbn):
    '''
        책 리뷰 리스트 CR

        ---
        GET -> 책 리뷰 리스트 가져오기
        POST -> 책에 리뷰 등록
    '''
    if request.method == 'GET':
        review_list = Review.objects.filter(book_isbn = book_isbn)
        serializer = ReviewSerializer(review_list, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    elif request.method == 'POST':
        request.data.update({'book_isbn': book_isbn})
        new_review = ReviewSerializer(data=request.data)
        if not new_review.is_valid(raise_exception=True):
            return Response({'message': 'Request Body Error'},
                            status=status.HTTP_409_CONFLICT)

        new_review.is_valid(raise_exception=True)  # 파라미터 : 유효성 검사, 실패시 예외 발생
        new_review.save()
        return Response(status=status.HTTP_201_CREATED)

# 리뷰 관련 API
@api_view(("PUT", "DELETE", ))
def review(request, review_id):
    '''
        리뷰 관련 UD

        ---
    '''
    if request.method == 'PUT':
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
        return Response(status = status.HTTP_202_ACCEPTED)

    elif request.method == "DELETE":
        post_instance = Review.objects.get(review_id=review_id)
        post_instance.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


# 유저가 쓴 리뷰 리스트
@api_view(("GET", ))
def user_review_list(request, user_id):
    '''
        유저 리뷰 리스트

        ---
        유저가 쓴 리뷰 리스트 반환
    '''
    user_review_list = Review.objects.filter(user_id=user_id)
    serializer = UserReviewSerializer(user_review_list, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)