from rest_framework import serializers
from .models import Book
from .models import Review, BooksSubcategory, BooksMaincategory
from django.db.models import Avg, Count

from accounts.models import User

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
    user_nickname = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['review_id', 'user_id', 'book_isbn', 'review_rating', 'review_content', 'review_date', 'user_nickname']

    def get_user_nickname(self, obj):
        return User.objects.get(id=obj.user_id).nickname

# 카테고리 검색할 때 쿼리 스트링을 위한 Query Serializer
class CategoryQuerySerializer(serializers.Serializer):
    main_id = serializers.IntegerField(help_text="주 카테고리의 id", required=False)
    sub_id  = serializers.IntegerField(help_text="서브 카테고리의 id", required=False)
    page    = serializers.IntegerField(help_text="페이지 넘버(한 페이지당 25개의 결과)", required=False)

# 책 검색을할 때 쿼리 스트링을 위한 Query Serializer
class BookSearchQuerySerializer(serializers.Serializer):
    TYPE_CHOICES =( 
        ("all", "all"), 
        ("title", "title"), 
        ("author", "author"), 
        ("description", "description"),
    )
    keyword = serializers.CharField(help_text="검색 키워드", required=False)
    search_type = serializers.ChoiceField(help_text="검색 타입", choices=TYPE_CHOICES,allow_blank=True, required=False) 
    page = serializers.IntegerField(help_text="페이지 넘버(한 페이지당 25개의 결과)", required=False)


class BookDetailSerializer(serializers.ModelSerializer):
    rating_avg = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            'book_id', 'book_isbn', 'book_title', 'book_author',
            'book_publisher', 'book_description', 'book_pages', 'book_price',
            'rating_avg', 'rating_count'
        ]

    def get_rating_avg(self, obj):
        return Review.objects.filter(book_isbn=obj.book_isbn).aggregate(Avg('review_rating'))

    def get_rating_count(self, obj):
        return Review.objects.filter(book_isbn=obj.book_isbn).aggregate(Count('review_rating'))

class UserReviewSerializer(serializers.ModelSerializer):
    book_title = serializers.SerializerMethodField()
    book_author = serializers.SerializerMethodField()
    rating_avg = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ['review_id', 'user_id', 'book_isbn', 'book_title', 'book_author',
                'review_content', 'review_date', 'rating_avg', 'rating_count']

    def get_book_title(self, obj):
        return Book.objects.get(book_isbn=obj.book_isbn).book_title

    def get_book_author(self, obj):
        return Book.objects.get(book_isbn=obj.book_isbn).book_author

    def get_rating_avg(self, obj):
        return Review.objects.filter(book_isbn=obj.book_isbn).aggregate(Avg('review_rating'))

    def get_rating_count(self, obj):
        return Review.objects.filter(book_isbn=obj.book_isbn).aggregate(Count('review_rating'))

# user_id Request Body
class UserIdSerializer(serializers.Serializer):
    user_id =serializers.IntegerField()