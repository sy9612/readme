from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('list', views.List_books.as_view()),
    path('search', views.search, name="search"),
    path('<int:book_id>/', views.detail, name='detail'),
]