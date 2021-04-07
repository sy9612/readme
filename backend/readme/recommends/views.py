import random
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import CollaborativeRecommendBook, ContentsBasedBooks, BestSeller
from books.models import Book, Review
from .serializers import RecommendBookSerializer
from books.serializers import BookSerializer
from .pagination import CarouselPageNumberPagination


@api_view(('GET', ))
def recommend_list(request, user_id):
    '''
        리뷰 개수에 따른 추천 책 리스트 반환

        ---
        ## 1. 리뷰의 개수가 10개 이상이면 협업 필터링
        ## 2. 1개 이상, 10개 미만이면 컨텐츠 기반 필터링
        ## 3. 리뷰 작성을 한 번도 안한 경우 or 로그인하지 않은 경우 베스트셀러
    '''
    count = Review.objects.filter(user_id=user_id).count()
    # 캐러셀 페이징. 16개의 결과를 뽑아줌
    paginator = CarouselPageNumberPagination()

    # 로그인 확인은 API Test 해볼 때 필요 없으니까 일단 주석처리
    # 로그인 되어있는 유저인지 확인
    # if request.user.is_authenticated:

    book_list = Book.objects.order_by('-book_id')

    if count >= 10:
        # 리뷰의 개수가 10개 이상이면 협업 필터링
        recommend_list = CollaborativeRecommendBook.objects.filter(
            user_id=user_id)

        recommend_book_list = book_list.filter(book_isbn__in=list(
            recommend_list.values_list('book_isbn', flat=True)))
    elif count >= 1:
        # 1개 이상, 10개 미만이면 컨텐츠 기반 필터링ff
        contentsRecommend_list = getContentsBasedRecommendBooks(user_id)
        recommend_book_list = book_list.filter(
            book_isbn__in=contentsRecommend_list)
    else:
        # 리뷰 작성을 한 번도 안한 경우 베스트셀러
        recommend_list = BestSeller.objects.all()
        recommend_book_list = book_list.filter(book_isbn__in=list(
            recommend_list.values_list('book_isbn', flat=True)))

    recommend_book_list = paginator.paginate_queryset(
        recommend_book_list, request)
    serializer = RecommendBookSerializer(recommend_book_list, many=True)
    # else:
    #     # 로그인이 되어있지 않으면 베스트셀러
    #     recommend_list = BestSeller.objects.all()
    #     recommend_book_list = Book.objects.filter(book_isbn__in = list(recommend_list.values_list('book_isbn', flat=True)))
    #     recommend_book_list = paginator.paginate_queryset(recommend_book_list, request)
    #     serializer = RecommendBookSerializer(recommend_book_list, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


def getContentsBasedRecommendBooks(user_id):
    # books_review 테이블에 있는 데이터중에서 user_id가 읽은 책 가져오기
    user_read_list = []
    user_read_list = Review.objects.filter(user_id=user_id)

    # user_read_list에 담긴 isbn마다 ContentsBasedBooks테이블로부터 동일한 main_isbn의 row의 isbn을 가져와 recomm_list에 담기
    recomm_list = []
    for obj in user_read_list:
        result = ContentsBasedBooks.objects.filter(main_isbn=obj.book_isbn)
        if result:
            recomm_list.append(result)

    # real_recomm_list = random.sample(recomm_list, 1)  # 한묶음당 책10권 추출
    change_list = []
    for query in recomm_list:
        for e in query:
            change_list.append(e.relative_isbn1)
            change_list.append(e.relative_isbn2)
            change_list.append(e.relative_isbn3)
            change_list.append(e.relative_isbn4)
            change_list.append(e.relative_isbn5)
            change_list.append(e.relative_isbn6)
            change_list.append(e.relative_isbn7)
            change_list.append(e.relative_isbn8)
            change_list.append(e.relative_isbn9)

    change_list = list(set(change_list))  # 중복원소 제거

    # change_list안에서 user_read_list에 없는 값 추출해서 real_recomm_list에 담기
    temp_recomm_list = []
    for sub in change_list:  # sub는 ContentsBasedBooks테이블의 row를 의미함
        if sub not in user_read_list:
            temp_recomm_list.append(sub)

    # print(temp_recomm_list)

    # temp_recomm_list의 원소들을 랜덤하게 10개 추출하여 real_recomm_list에 담기
    real_recomm_list = []
    if len(temp_recomm_list) <= 10:
        real_recomm_list = temp_recomm_list
    else:
        real_recomm_list = random.sample(temp_recomm_list, 10)  # 10개 추출

    return real_recomm_list
