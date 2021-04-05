from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('signup', views.Registration.as_view()),
    path('login', obtain_jwt_token),
    path('<int:user_id>', views.account_update_delete, name='account_update_delete'),
    path('dibsList', views.dibsList, name="dibsList"),
    path('clickDibs/<int:book_isbn>', views.clickDibs, name="clickDibs"),
]
