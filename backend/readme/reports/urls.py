from django.urls import path, include
from . import views

urlpatterns = [
    # ex: /reports/10
    path('<int:user_id>', views.report, name='report'),
    # ex: /reports/10/5
    path('<int:user_id>/<int:book_id>', views.report_detail, name='report_detail')
]