"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_url_patterns = [
    path('rest_api/', include('rest_api.urls')),
]


schema_view = get_schema_view(
    openapi.Info(
        title="KNOWHOW Swagger",
        default_version="v1",
        description="KNOWHOW Rest api 문서",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="pyhpyh0670@gmail.com"),
        license=openapi.License(name="GNU General Public License v2.0"),
    ),
    validators=['flex'],
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=schema_url_patterns,
)


urlpatterns = [
    path('admin', admin.site.urls),
    path('rest_api/', include('rest_api.urls')),
]


if settings.DEBUG:
    urlpatterns = [
        path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name="schema-json"),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
