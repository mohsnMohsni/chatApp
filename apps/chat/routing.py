# Core imports.
from django.urls import path

from .consumers import ChatWebsocketConsumer


websocket_urlpatterns = [
    path('ws/chat/<str:room_name>/', ChatWebsocketConsumer.as_asgi(), name='chat-consumer'),
]
