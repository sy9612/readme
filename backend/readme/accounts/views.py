from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status, mixins
from rest_framework import generics  #generios class-based view 사용
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from django.utils import timezone

#JWT 사용을 위해 필요
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer

from .serializers import *
from .models import *
from books.models import Book, Report, Review

#user update에 사용
from .forms import CustomUserChangeForm
from django.db.models import Q

# drf_yasg
from drf_yasg.utils import swagger_auto_schema


#누구나 접근 가능하다는 의미
@permission_classes([AllowAny])
class Registration(generics.GenericAPIView):
    serializer_class = CustomRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({'message': 'Request Body Error'},
                            status=status.HTTP_409_CONFLICT)

        serializer.is_valid(raise_exception=True)
        user = serializer.save(request)  #애는 request 필요...없으면 오류..

        return Response(
            {
                "user":
                UserSerializer(
                    #get_serializer_context : serializer에 포함되어야 할 정보의 context들을 딕셔너리 형태로 리턴
                    user,
                    context=self.get_serializer_context()).data
            },
            status=status.HTTP_201_CREATED,
        )


# @permission_classes([AllowAny])
# class Login(generics.GenericAPIView):
#     serializer_class = UserLoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)

#         if not serializer.is_valid(raise_exception=True):
#             return Response({'message': 'Request Body Error'},
#                             status=status.HTTP_409_CONFLICT)

#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data

#         if user['username'] == 'None':
#             return Response({'message': 'Fail'},
#                             status=status.HTTP_401_UNAUTHORIZED)

#         return Response({
#             "user":
#             UserSerializer(
#                 #get_serializer_context : serializer에 포함되어야 할 정보의 context들을 딕셔너리 형태로 리턴
#                 user,
#                 context=self.get_serializer_context()).data,
#             "token":
#             user['token']
#         })

@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
@swagger_auto_schema(method='put', request_body=UserChangeSerializer)
@api_view(('GET', 'PUT', 'DELETE'))
def account_update_delete(request, user_id):
    '''
        유저 관련 RUD
        
        ---
    '''

    user = get_object_or_404(User, pk=user_id)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'PUT':
        # print(request.data)
        user_change_form = CustomUserChangeForm(request.data, instance = user)
        if user_change_form.is_valid():
            user_change_form.save()
            return Response(user_change_form.data, status = status.HTTP_202_ACCEPTED)
        return Response(user_change_form.errors, status = status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


#user별 찜 리스트
@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
@api_view(('GET', ))
def dibs_list(request, user_id):
    """
        user별 찜 리스트

        ---
        # Response
            - book_id     : 책 id
            - book_isbn   : isbn
            - book_title  : 제목
            - book_author : 저자

            - rating_avg   : 평균별점
            - rating_count : 리뷰개수
    """
    dib_list = Dibs.objects.filter(Q(is_selected=1) & Q(user_id=user_id))

    book_list = Book.objects.filter(book_isbn__in=list(dib_list.values_list('book_isbn', flat=True)))
    serializer = UserBookSerializer(book_list, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@permission_classes((IsAuthenticated, ))
@authentication_classes((JSONWebTokenAuthentication,))
@api_view(('GET', ))
def review_report_list(request, user_id):
    '''
        user별 읽은 책 리스트

        ---
        ## (report_list + review_list) 에서 중복제거한 리스트 
        # Response
            - book_id     : 책 id
            - book_isbn   : isbn
            - book_title  : 제목
            - book_author : 저자

            - rating_avg   : 평균별점
            - rating_count : 리뷰개수
    '''
    read_list = []
    report_list = Report.objects.filter(user_id = user_id)
    review_list = Review.objects.filter(user_id = user_id)

    read_list.extend(list(report_list.values_list('book_isbn', flat=True)))
    read_list.extend(list(review_list.values_list('book_isbn', flat=True)))
    read_set = set(read_list)   # isbn 중복제거
    read_list = list(read_set)
    read_book_list = Book.objects.filter(book_isbn__in = read_list)
    serializer = UserBookSerializer(read_book_list, many=True)

    return Response(serializer.data, status = status.HTTP_200_OK)


@api_view(('POST', ))
def clickDibs(request, book_isbn):
    #일단 book_id와 user_id가 같은 dibs 목록에 is_selected가 1 인지 확인
    #1이면 0으로 바꿔주고
    #0이면 1로 바꿔주고
    #없으면 1로 데이터 생성
    #int n = select count(dibs_id) from Dibs where user_id=1 and book_id=1
    user_id = request.data['user_id']
    isSelected = Dibs.objects.filter(Q(book_isbn=book_isbn) & Q(user_id=user_id))

    List = []
    if isSelected:
        print("존재해!")
        List = list(isSelected.values())
        #print(List[0])
        if List[0]['is_selected'] == 1:
            #if n>0
            #update 1->0
            print("1이야!")
            instance = Dibs.objects.get(dibs_id=List[0]['dibs_id'])
            instance.is_selected = 0
            instance.save()
            return Response(
                {
                    "dibSelect": False,
                },
                status=status.HTTP_200_OK,
            )
        else:
            #update 0->1
            print("0이야!")
            instance = Dibs.objects.get(dibs_id=List[0]['dibs_id'])
            instance.is_selected = 1
            instance.save()
            return Response(
                {
                    "dibSelect": True,
                },
                status=status.HTTP_200_OK,
            )
    else:
        #else
        #insert into
        print("존재하지 않아!")
        ######일단 시간이 지금 UTC?로 되어있긴 한데...
        new_dib = Dibs.objects.create(user_id=user_id,
                                      book_isbn=book_isbn,
                                      dibs_date=timezone.now(),
                                      is_selected=1)
        return Response(
            {
                "dibSelect": True,
            },
            status=status.HTTP_200_OK,
        )