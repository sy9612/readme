#adaper를 제대로 사용하기 위해서 생성

# 1. 사용자가 회원가입할 때 nickname, introduction을 입력하도록 설정
# get_cleaned_data 함수에 필요한 정보를 추가로 입력해서 커스터마이징

from rest_framework import serializers
from allauth.account.adapter import get_adapter
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login
from django.contrib.auth import authenticate
from rest_auth.registration.serializers import RegisterSerializer

from .models import *

#JWT 사용을 위한 설정
JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()  # 기본 유저 모델 가져오기


#회원가입
class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=False, max_length=50)
    introduction = serializers.CharField(required=False, max_length=200)
    gender = serializers.CharField(required=True, max_length=5)
    mbti_id = serializers.IntegerField(required=False)

    def get_cleaned_data(self):
        #username, password, email이 default라는 뜻(?)
        data_dict = super().get_cleaned_data()
        data_dict['nickname'] = self.validated_data.get('nickname', '')
        data_dict['introduction'] = self.validated_data.get('introduction', '')
        data_dict['gender'] = self.validated_data.get('gender', '')
        data_dict['mbti_id'] = self.validated_data.get('mbti_id', '')
        return data_dict


#로그인
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password', None)
        #사용자 아이디와 비밀번호로 로그인 구현!!
        #email로 하고 싶으면 username을 email로 바꾸면 될듯?

        user = authenticate(username=username, password=password)

        if user is None:
            return {'username': 'None'}

        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)

        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given username and password does not exist')
        #잘 나온다... 흠냐..흠 ?
        return {'username': user.username, 'token': jwt_token}


#사용자 정보 추출?
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'nickname', 'introduction', 'gender',
                  'mbti_id')
