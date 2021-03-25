from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.Registration.as_view()),
    path('login', views.Login.as_view()),
    #path('update/', views.update, name='update'),
    path('dibsList', views.dibsList, name="dibsList"),
]
