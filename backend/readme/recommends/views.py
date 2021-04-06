from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from .models import CollaborativeRecommendBook, ContentRecommendBook, BestSeller
from .serializers import RecommendBookSerializer, BestSellerSerializer

import os
import sys
sys.path.append( os.path.dirname(os.path.abspath(os.path.dirname(__file__))) )
from books.models import Book, Review
from books.serializers import BookSerializer

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
    # 로그인 되어있는 유저인지 확인
    if request.user.is_authenticated:
        if count >= 10:
            # 리뷰의 개수가 10개 이상이면 협업 필터링
            recommend_list = CollaborativeRecommendBook.objects.filter(user_id=user_id)
        elif count >= 1:
            # 1개 이상, 10개 미만이면 컨텐츠 기반 필터링
            recommend_list = ContentRecommendBook.objects.filter(user_id=user_id)
        else:
            # 리뷰 작성을 한 번도 안한 경우 베스트셀러
            recommend_list = BestSeller.objects.all()
        recommend_book_list = Book.objects.filter(book_isbn__in = list(recommend_list.values_list('book_isbn', flat=True)))
        serializer = BookSerializer(recommend_book_list, many=True)
    else:
        # 로그인이 되어있지 않으면 베스트셀러
        recommend_list = BestSeller.objects.all()
        serializer = BestSellerSerializer(recommend_list, many=True)
    

    return Response(serializer.data, status=status.HTTP_200_OK)
