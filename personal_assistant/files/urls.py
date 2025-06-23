"""URL configuration for the files app."""

from django.urls import path
from .views import file_manager

urlpatterns = [
    path("", file_manager, name="file-manager"),
]