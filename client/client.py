import asyncio
import websockets

async def receive_poll_data():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            # Receive poll data from server
            poll_data = await websocket.recv()
            print("Received poll data:", poll_data)

asyncio.get_event_loop().run_until_complete(receive_poll_data())
