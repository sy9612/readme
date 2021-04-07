from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_auth.views import (LoginView, LogoutView, PasswordChangeView,
                             PasswordResetView, PasswordResetConfirmView)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Readme API",
        default_version="v1",
        description="ReadME 개발자들을 위한 API 문서",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(name="test", email="test@test.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin', admin.site.urls),
    #path('accounts/', include('accounts.urls')),
    #path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    path('books/', include('books.urls')),
    path('reports/', include('reports.urls')),
    path('mbtis/', include('mbtis.urls')),
    path('recommends/', include('recommends.urls')),
    # 로그인 - 주어진 view로 테스트
    # path('rest-auth/login', LoginView.as_view(), name='rest_login'),
    # path('rest-auth/logout', LogoutView.as_view(), name='rest_logout'),
    # path('rest-auth/password/change',
    #      PasswordChangeView.as_view(),
    #      name='rest_password_change'),
]

if settings.DEBUG:
    urlpatterns = [
        # ...
        path('swagger<str:format>', schema_view.without_ui(
            cache_timeout=0), name='schema-json'),
        path('swagger/', schema_view.with_ui('swagger',
                                             cache_timeout=0), name='schema-swagger-ui'),
        path('docs/', schema_view.with_ui('redoc',
                                          cache_timeout=0), name='schema-redoc'),
        # ...
    ] + urlpatterns
