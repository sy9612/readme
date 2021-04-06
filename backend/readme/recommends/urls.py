from django.urls import path, include
from . import views

urlpatterns = [
    # ex: /recommends/1/list
    path('<int:user_id>/list', views.recommend_list, name="recommend_list"),
]