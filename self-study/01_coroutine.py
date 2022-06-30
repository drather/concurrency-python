import asyncio
import time
from datetime import datetime


async def main1():
    print("hello")
    await asyncio.sleep(1)
    print("world")


async def say_after(delay, what):
    print(f"now: {datetime.now()}")
    await asyncio.sleep(delay)
    print(what)

async def main2():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


async def main3():
    task1 = asyncio.create_task(say_after(1, 'hello'))

    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(main3())

