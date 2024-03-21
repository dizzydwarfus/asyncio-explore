import asyncio


async def task(name, delay):
    await asyncio.sleep(delay)
    print(f"Task {name} finished after {delay}s")


async def main():
    await asyncio.gather(task("A", 5), task("B", 1), task("C", 3))


asyncio.run(main())
