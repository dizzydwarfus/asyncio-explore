import asyncio


async def background_task():
    while True:
        print("Background task running...")
        await asyncio.sleep(2)


async def main():
    task = asyncio.create_task(background_task())
    # Do some other work here
    await asyncio.sleep(5)  # Simulate other work
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Background task was cancelled")


asyncio.run(main())
