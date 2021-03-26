from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = [
        #     'book_id', 'book_isbn', 'book_title', 'book_author',
        #     'book_publisher', 'book_description', 'book_pages', 'book_price'
        # ]
