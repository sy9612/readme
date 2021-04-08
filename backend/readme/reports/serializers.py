from rest_framework import serializers
from books.models import Report, Review, Book
from django.db.models import Avg, Count


class ReportSerializer(serializers.ModelSerializer):
    book_title = serializers.SerializerMethodField()
    rating_avg = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = ['book_isbn', 'book_title', 'rating_avg', 'rating_count']

    def get_book_title(self, obj):
        return Book.objects.get(book_isbn=obj.book_isbn).book_title

    def get_rating_avg(self, obj):
        return Review.objects.filter(book_isbn=obj.book_isbn).aggregate(Avg('review_rating'))

    def get_rating_count(self, obj):
        return Review.objects.filter(book_isbn=obj.book_isbn).aggregate(Count('review_rating'))


class ReportDetailSerializer(serializers.ModelSerializer):
    book_title = serializers.SerializerMethodField()
    rating_avg = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()

    class Meta:
        model = Report
        fields = ['book_isbn', 'book_title', 'report_content', 'rating_avg', 'rating_count']

    def get_book_title(self, obj):
        return Book.objects.get(book_isbn=obj.book_isbn).book_title

    def get_rating_avg(self, obj):
        return Review.objects.filter(book_isbn=obj.book_isbn).aggregate(Avg('review_rating'))

    def get_rating_count(self, obj):
        return Review.objects.filter(book_isbn=obj.book_isbn).aggregate(Count('review_rating'))