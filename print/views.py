from django.shortcuts import render
import asyncio, websockets, json, requests


URI = 'ws://octoprint:5000/sockjs/websocket'

# Create your views here.

def get_session(api_key):
    hed = {'Authorization': 'Bearer ' + api_key}
    data = {'passive' : 1}

    url = 'http://octoprint:5000/api/login'
    response = requests.post(url,data=data, headers=hed)
    print(json.loads(response.text)["session"])

    #return session id
    return json.loads(response.text)["session"]

async def start_connection(api_key, user):
    auth = {"auth": user+":"+get_session(api_key)}
    async with websockets.connect(URI) as websocket:
        #authorize
        await websocket.send(json.dumps(auth))
        await websocket.recv()
    async for message in websocket:
        print(message)

def init_connection(api_key, user):
    asyncio.get_event_loop().run_until_complete(
        start_connection(api_key, user)
    )
