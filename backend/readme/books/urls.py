from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('list', views.booklist),
    path('search', views.search, name="search"),
    path('<int:book_id>', views.detail, name='detail'),
    path('createReview', views.createReview, name="createReview"),
    path('updateReview/<int:review_id>',
         views.updateReview,
         name="updateReview"),
    path('deleteReview/<int:review_id>',
         views.deleteReview,
         name="deleteReview"),
]