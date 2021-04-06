from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('list', views.book_list, name="book_list"),
    path('search', views.search, name="search"),
    path('<int:book_isbn>', views.detail, name='detail'),
    path('review/<int:review_id>', views.review, name='review'),
    path('maincategory', views.maincategory, name="maincategory"),
    path('subcategory/<int:main_id>', views.subcategory, name="subcategory"),
    path('categorySearch', views.category_search, name="category_search")
]