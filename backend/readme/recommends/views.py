from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import CollaborativeRecommendBook, ContentRecommendBook, BestSeller
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
    if count >= 10:
        # 리뷰의 개수가 10개 이상이면 협업 필터링
        recommend_list = CollaborativeRecommendBook.objects.filter(user_id=user_id)
    elif count >= 1:
        # 1개 이상, 10개 미만이면 컨텐츠 기반 필터링
        recommend_list = ContentRecommendBook.objects.filter(user_id=user_id)
    else:
        # 리뷰 작성을 한 번도 안한 경우 베스트셀러
        recommend_list = BestSeller.objects.all()

    book_list = Book.objects.order_by('-book_id')
    recommend_book_list = book_list.filter(book_isbn__in = list(recommend_list.values_list('book_isbn', flat=True)))
    recommend_book_list = paginator.paginate_queryset(recommend_book_list, request)
    serializer = RecommendBookSerializer(recommend_book_list, many=True)
    # else:
    #     # 로그인이 되어있지 않으면 베스트셀러
    #     recommend_list = BestSeller.objects.all()
    #     recommend_book_list = Book.objects.filter(book_isbn__in = list(recommend_list.values_list('book_isbn', flat=True)))
    #     recommend_book_list = paginator.paginate_queryset(recommend_book_list, request)
    #     serializer = RecommendBookSerializer(recommend_book_list, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)
