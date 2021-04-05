from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('signup', views.Registration.as_view()),
    path('login', obtain_jwt_token),
    path('<int:user_id>', views.account_update_delete, name='account_update_delete'),
    path('<int:user_id>/dibsList', views.dibs_list, name="dibs_list"),
    path('clickDibs/<int:book_id>', views.clickDibs, name="clickDibs"),
]
