import websockets
import asyncio


async def message():
    async with websockets.connect("ws://localhost:8765") as socket:
        msg = input("What's your message? ")
        await socket.send(msg)
        print(await socket.recv())


if __name__ == "__main__":
    while True:
        asyncio.run(message())
