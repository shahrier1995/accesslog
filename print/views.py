from django.shortcuts import render
import asyncio, websockets, json, octorest

from websockets import client

API_KEY = "0DA5AB1556C843C08E82012A3C8BBEAE"
URI = 'ws://octoprint:5000/sockjs/websocket'

# Create your views here.


async def start_connection():
    request = {"apikey": API_KEY}
    async with websockets.connect(URI) as websocket:
        await websocket.send(json.dumps(request))
        await websocket.recv()

def init_connection():
    asyncio.get_event_loop().run_until_complete(
        start_connection()
    )