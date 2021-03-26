from django.shortcuts import render
from .models import Book  #models에 테이블 관련 class 가져오기?
from .models import Review
from django import forms
from django.views import generic  #django에 있는 기본 view로 테스트
from django.views.generic.edit import FormView
from django.db.models import Q
from django.utils import timezone
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse


class List_books(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'book_list.html'
        book_list = Book.objects.all()  #BooksBook 테이블의 모든 정보 가져오기
        print(book_list)
        return render(request, template_name, {"book_list": book_list})
        #딕셔너리? 형식으로 전달한다고 함


# 모든 책을 가져오고나서 .. .. 검색인데 ㅇㅁㅇ
def search(request):
    books = Book.objects.all().order_by('-book_id')
    contents = request.POST.get('contents', "")

    if contents:
        books = books.filter(
            Q(book_title__icontains=contents)
            | Q(book_author__icontains=contents)
            | Q(book_subcategory__icontains=contents)).distinct()
        #Q객체 : filter()메소드의 조건을 다양하게 줄 수 있음
        #icontains 연산자 : 대소문자를 구분하지 않고 단어가 포함되어있는지 검사
        #distinct() : 중복된 객체 제외

        return render(request, 'search_book.html', {
            'books': books,
            'contents': contents
        })

    else:
        return render(request, 'search_book.html')


#도서 상세 정보
def detail(request, book_id):
    book = Book.objects.get(book_id=book_id)
    context = {
        'book': book,
    }
    #리뷰 작성했는지 확인하는 sql 필요
    #여기서 리뷰를 작성한 사람이면 "리뷰작성함" 메시지를 보내야하고
    isWriten = Review.objects.filter(Q(book_id=1) & Q(user_id=1))
    if isWriten:
        print("작성한 리뷰 내용 전송")  #화면에 띄워주기 편하려고!
    #리뷰를 작성하지 않은 사람이면 "리뷰작성안함" 메시지를 보내서 리뷰작성 버튼을 만들어야지
    else:
        print("리뷰를 작성하지 않았다는 메시지 전송")

    #리뷰 작성 여부를 같이 보내야하지 않을까?
    #
    return render(request, '../templates/detail.html', context)

    #return Response(book)


#리뷰 작성
def createReview(request):
    new_review = Review.objects.create(user_id=1,
                                       book_id=1,
                                       review_rating=3,
                                       review_content="리뷰내용내용내용",
                                       revie_date=timezone.now())


#리뷰 수정
def updateReview(request):
    #request로 들어오는 review_id
    instance = Review.objects.get(review_id=1)
    instance.review_rating = 4
    instance.review_content = "바뀐 리뷰 내용내용"
    instance.review_date = timezone.now()
    instance.save()