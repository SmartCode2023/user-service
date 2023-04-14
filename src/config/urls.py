from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve

# Swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="#USER SERVICE REST API",
        default_version="v1",
        description="USER API REST for Arquitectura de Software. Created: PUJ.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="paladavid@hotmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# Importing apps urls
from apps.users.api.urls import urlpatterns as users_urls

# API urls
urlpatterns = [
    # Swagger urls
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
    path("admin/", admin.site.urls),
    path("api/auth/", include("apps.authentication.api.urls")),
    path("api/users/", include(users_urls)),
]

# Media files
urlpatterns += [
    re_path(
        r"^media/(?P<path>.*)$",
        serve,
        {
            "document_root": settings.MEDIA_ROOT,
        },
    ),
]
