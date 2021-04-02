from rest_framework import serializers
from .models import Book
from .models import Review, BooksSubcategory, BooksMaincategory


#책 전체 정보를 가져올 때
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = [
        #     'book_id', 'book_isbn', 'book_title', 'book_author',
        #     'book_publisher', 'book_description', 'book_pages', 'book_price'
        # ]


class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksMaincategory
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksSubcategory
        fields = '__all__'


#리뷰 데이터 가져올 때
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user_id', 'book_id', 'review_rating', 'review_content']

# 카테고리 검색할 때 쿼리 스트링을 위한 Query Serializer
class CategoryQuerySerializer(serializers.Serializer):
    main_id = serializers.IntegerField(help_text="주 카테고리의 id", required=False)
    sub_id  = serializers.IntegerField(help_text="서브 카테고리의 id", required=False)
    page    = serializers.IntegerField(help_text="페이지 넘버(한 페이지당 25개의 결과)", required=False)