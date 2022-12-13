# Core imports.
from django.urls import path, re_path

from .consumers import ChatWebsocketConsumer


websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', ChatWebsocketConsumer.as_asgi()),
    # path('ws/chat/<str:room_name>/', ChatWebsocketConsumer.as_asgi(), name='chat-consumer'),
]
