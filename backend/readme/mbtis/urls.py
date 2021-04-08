from django.urls import path, include
from . import views

urlpatterns = [
    # ex: /mbtis/3
    path('<int:user_id>', views.mbti_book_list, name='mbti_book_list'),
]
