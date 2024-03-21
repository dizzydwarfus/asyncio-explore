import asyncio
from websockets.server import serve


async def response(websocket, path):
    message = await websocket.recv()
    print(f"Received: {message}")
    await websocket.send("I received your message!")


async def main():
    async with serve(response, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
