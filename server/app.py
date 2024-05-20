import asyncio
import websockets

# Store poll data
poll_data = {
    "question": "What is your favorite programming language?",
    "options": {
        "Python": 0,
        "JavaScript": 0,
        "Java": 0,
        "C++": 0
    }
}

# Function to handle incoming WebSocket connections
async def handle_connection(websocket, path):
    try:
        async for message in websocket:
            # Receive message from client (if needed)
            print(f"Received message from client: {message}")

            # Send poll data to client
            await websocket.send(poll_data)
    except websockets.exceptions.ConnectionClosedError:
        print("Connection closed unexpectedly")

# Start WebSocket server
start_server = websockets.serve(handle_connection, "localhost", 8765)

# Run event loop
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
