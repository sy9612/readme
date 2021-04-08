from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import MBTI, MBTIBook
from .serializers import MbtiBookSerializer
from books.models import Book
from accounts.models import User


@api_view(('GET', ))
def mbti_book_list(request, user_id):
    '''
        MBTI별 추천 도서 리스트 반환

        ---
    '''
    mbti_id = User.objects.get(id=user_id).mbti_id

    mbti_type = MBTI.objects.get(mbti_id=mbti_id).mbti_type
    mbti_type_list = list(mbti_type)

    mbti_book_list = MBTIBook.objects.filter(one_of_mbti_type__in = mbti_type_list)
    mbti_book_list = Book.objects.filter(book_isbn__in=list(
        mbti_book_list.values_list('book_isbn', flat=True)))
    serializer = MbtiBookSerializer(mbti_book_list, many=True)

    return Response({
        "mbti_type": mbti_type,
        "mbti_book_list": serializer.data,
    }, status=status.HTTP_200_OK)
