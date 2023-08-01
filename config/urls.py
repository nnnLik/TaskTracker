from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

from src.router import routes

schema_view = get_schema_view(
    openapi.Info(
        title="TaskTracker API",
        default_version="v3.1.3",
        description="TaskTracker Api implementation",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("admin/", admin.site.urls),
    path("api/", include(routes)),
    path(
        "swagger/",
        schema_view.with_ui("swagger"),
        name="schema-swagger-ui",
    ),
]

urlpatterns += static(settings.VIDEO_URL, document_root=settings.VIDEO_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
