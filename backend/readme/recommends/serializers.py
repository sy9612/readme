from rest_framework import serializers
import os
import sys
sys.path.append( os.path.dirname(os.path.abspath(os.path.dirname(__file__))) )
from books.models import Book, Review

# 추천 리스트에 보여지는 책 정보 Serializer
class RecommendBookSerializer(serializers.ModelSerializer):
    rating_avg = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['book_id', 'book_isbn', 'book_title', 'book_author', 'rating_avg']

    def get_rating_avg(self, obj):
        return Review.objects.filter(book_isbn=obj.book_isbn).aggregate(Avg('review_rating'))

class BestSellerSerializer(serializers.ModelSerializer):
    rating_avg = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['book_id', 'book_isbn', 'book_title', 'book_author', 'rating_avg']

    def get_rating_avg(self, obj):
        return Review.objects.filter(book_isbn=obj.book_isbn).aggregate(Avg('review_rating'))