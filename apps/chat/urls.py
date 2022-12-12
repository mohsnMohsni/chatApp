# Core imports.
from django.urls import path

from .views import room_view, index_view


urlpatterns = [
    path('', index_view, name='chat-index'),
    path('<str:room_name>/', room_view, name='chat-room'),
]
