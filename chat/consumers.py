import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async


class ChatConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print("connected: ", event)
        self.chat_room = "ibu"
        await self.channel_layer.group_add(
            "ibu",
            self.channel_name

        )

        print(self.channel_name)
        await self.send(
            {
                'type':'websocket.accept'
            }
        )


    async def websocket_disconnect(self, event):
       
        print("chat dickens disconnnect: ", event)

    async def websocket_receive(self, event):
        
        print("receive: ", event)
        obj = event['text']

        await self.channel_layer.group_send("ibu",
             {
                'type':'chat_message',
                'text': obj
             }
        )
        
      
    async def chat_message(self, event):
        await self.send(
            {
                'type':'websocket.send',
                'text': event['text'],
            }
        )