import ssl

import aiohttp
import time
import asyncio

import certifi


async def fetcher(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    conn = aiohttp.TCPConnector(ssl=ssl_context)

    async with aiohttp.ClientSession(connector=conn) as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)


if __name__ == "__main__":

    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)  # 4.8