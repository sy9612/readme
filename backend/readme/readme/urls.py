from django.contrib import admin
from django.urls import path, include
from rest_auth.views import (LoginView, LogoutView, PasswordChangeView,
                             PasswordResetView, PasswordResetConfirmView)

urlpatterns = [
    path('admin', admin.site.urls),
    #path('accounts/', include('accounts.urls')),
    #path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    path('books/', include('books.urls')),
    path('reports/', include('reports.urls')),
    # 로그인 - 주어진 view로 테스트
    # path('rest-auth/login', LoginView.as_view(), name='rest_login'),
    # path('rest-auth/logout', LogoutView.as_view(), name='rest_logout'),
    # path('rest-auth/password/change',
    #      PasswordChangeView.as_view(),
    #      name='rest_password_change'),
]
