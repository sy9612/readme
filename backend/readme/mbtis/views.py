from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import MBTI, MBTIBook
from .serializers import MbtiBookSerializer
# 상위 폴더 import
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from books.models import Book


@api_view(('GET', ))
def mbti_book_list(request, mbti_id):
    mbti_desc = MBTI.objects.get(mbti_id=mbti_id).mbti_desc

    mbti_book_list = MBTIBook.objects.filter(mbti_id=mbti_id)
    mbti_book_list = Book.objects.filter(book_isbn__in = list(mbti_book_list.values_list('book_isbn', flat=True)))
    serializer = MbtiBookSerializer(mbti_book_list, many=True)

    return Response({
        "mbti_desc": mbti_desc,
        "mbti_book_list": serializer.data,
    }, status=status.HTTP_200_OK)
