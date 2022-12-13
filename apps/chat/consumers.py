# Standard imports
import json

# Third-party imports.
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import RoomModel, MessageModel


class ChatWebsocketConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.room_name = None
        self.room_group_name = None
        self.room = None
        self.user = None

    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.room = RoomModel.objects.get(name=self.room_name)
        self.user = self.scope['user']

        self.accept()

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        if not self.user.is_authenticated:
            return

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'user': self.user.username,
                'message': message,
            },
        )
        MessageModel.objects.create(user=self.user, room=self.room, content=message)

    def chat_message(self, event):
        self.send(text_data=json.dumps(event))
