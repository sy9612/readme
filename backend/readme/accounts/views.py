from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, mixins
from rest_framework import generics  #generios class-based view 사용
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import permission_classes, authentication_classes

#JWT 사용을 위해 필요
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer

from .serializers import *
from .models import *
from books.models import Book

#user update에 사용
from .forms import CustomUserChangeForm
from django.db.models import Q


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
        user = serializer.save(request)  #request 필요...없으면 오류..

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


@permission_classes([AllowAny])
class Login(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response({'message': 'Request Body Error'},
                            status=status.HTTP_409_CONFLICT)

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        if user['username'] == 'None':
            return Response({'message': 'Fail'},
                            status=status.HTTP_401_UNAUTHORIZED)

        return Response({
            "user":
            UserSerializer(
                #get_serializer_context : serializer에 포함되어야 할 정보의 context들을 딕셔너리 형태로 리턴
                user,
                context=self.get_serializer_context()).data,
            "token":
            user['token']
        })


# def update(request):
#     if request.method == 'POST':
#         user_change_from = CustomUserChangeForm(request.POST)
#         if user_change_form.is_valid():
#             user_change_form.save()
#             return redirect('accounts:people', request.user.username)

#     else:
#         user_change_form = CustomUserChangeForm(instance=request.user)

#     return render(request, '../templates/update.html',
#                   {'user_change_form': user_change_form})


#user별 찜 리스트
def dibsList(request):
    #여기에 user_id가 로그인한 사람이 나와야함!
    #찜 목록에 있는 book_id를 가져와서 dibs에 넣어줌
    bookIdxs = Dibs.objects.filter(Q(is_selected=1)
                                   & Q(user_id=1)).values('book_id')
    contents = request.POST.get('contents', "")

    dibs = []
    for idx in bookIdxs:
        book = list(Book.objects.filter(Q(book_id=idx['book_id'])).values())
        print(book)
        dibs += book
    return render(request, 'dibs_list.html', {
        'dibs': dibs,
    })
