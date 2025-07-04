"""
URL Configuration for chat app.
"""

from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chat_view, name='chat'),
]
