from rest_framework import serializers
# 상위 폴더 import
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from books.models import Book


class MbtiBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['book_id', 'book_title', 'book_author', 'book_publisher']
