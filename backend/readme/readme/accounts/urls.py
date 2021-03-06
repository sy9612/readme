from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('signup', views.Registration.as_view()),
    path('login', obtain_jwt_token),
    #path('update/', views.update, name='update'),
    path('dibsList', views.dibsList, name="dibsList"),
]
