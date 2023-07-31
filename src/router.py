from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


routes = [
    path("todo/", include("src.todo.urls"), name="todo"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
