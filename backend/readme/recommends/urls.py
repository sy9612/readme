from django.urls import path, include
from . import views

urlpatterns = [
    # ex: /recommends/1/list
    path('<int:user_id>/list', views.recommend_list, name="recommend_list"),
    # ex: /recommends/agegender/1/list
    path('agegender/<int:user_id>/list', views.age_gender_recommend_list, name="age_gender_recommend_list"),
]