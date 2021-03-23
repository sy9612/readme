from django.shortcuts import render
from .models import Book  #models에 테이블 관련 class 가져오기?
from django import forms
from django.views import generic  #django에 있는 기본 view로 테스트
from django.views.generic.edit import FormView
from django.db.models import Q


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
            Q(book_name__icontains=contents)
            | Q(book_author__icontains=contents)
            | Q(book_category__icontains=contents)).distinct()
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
    return render(request, '../templates/detail.html', context)
