from rest_framework import serializers
from books.models import Book, Review
from django.db.models import Avg, Count

# 추천 리스트에 보여지는 책 정보 Serializer
class RecommendBookSerializer(serializers.ModelSerializer):
    rating_avg = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['book_id', 'book_isbn', 'book_title', 'book_author', 'rating_avg', 'rating_count']

    def get_rating_avg(self, obj):
        return Review.objects.filter(book_isbn=obj.book_isbn).aggregate(Avg('review_rating'))

    def get_rating_count(self, obj):
        return Review.objects.filter(book_isbn=obj.book_isbn).aggregate(Count('review_rating'))