from django.urls import path, include
from . import views

urlpatterns = [
    # ex: /reports/list/
    path('list', views.report_list, name='report_list'),
    # ex: /reports/create
    path('create', views.create_report, name='create_report'),
    # ex: /reports/5
    path('<int:book_id>', views.report_detail, name='report_detail')
]