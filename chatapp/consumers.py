from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async


'''
This class is a subclass of AsyncWebsocketConsumer, 
which is a class that handles WebSocket connections.
''' 
class ChatConsumer(AsyncWebsocketConsumer):

    # Establish connection with WebSocket
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # Accept connection
        await self.accept()
    

    # Disconnect from WebSocket
    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.channel_layer,
            self.room_group_name
        )

