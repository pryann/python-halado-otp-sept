import asyncio
import aiohttp
from time import sleep


async def get_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


# async def send_with_limit(urls, delay=1):
#     tasks = []
#     for url in urls:
#         tasks.append(get_request(url))
#     responses = await asyncio.gather(*tasks)
#     sleep(delay)
#     return responses


async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/comments/1",
        "https://jsonplaceholder.typicode.com/todos/1",
    ]

    # for i in range(0, len(urls, 40)):
    # can raise Iterationerror
    #     send_with_limit(urls[i : i + 40])

    tasks = [get_request(url) for url in urls]

    responses = await asyncio.gather(*tasks)
    for response in responses:
        print(response, end="\n\n")


if __name__ == "__main__":
    asyncio.run(main())
