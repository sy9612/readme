from rest_framework import serializers
from books.models import Book


class MbtiBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['book_isbn', 'book_title', 'book_author', 'book_publisher']
