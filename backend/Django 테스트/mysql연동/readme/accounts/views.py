from django.shortcuts import render
from .models import AuthUser  #Post모델 불러오기

def post_view(request):
    posts = AuthUser.objects.all()  #post 테이블의 모든 객체 불러와서 posts 변수에 저장
    return render(request,'index.html',{"posts":posts})
