import asyncio
from time import perf_counter


async def get_http_request():
    print("starting GET http request")
    await asyncio.sleep(2)
    print("http GET request done")
    return "response from server"


async def post_http_request(data):
    print("starting http POST request")
    await asyncio.sleep(4)
    print("http POST request done")
    return data


# SERIAL VERSION
# async def main():
#     print(f"Get: {await get_http_request()}")
#     print(f"Post: {await post_http_request('some data')}")


# "PARALLEL" VERSION, NOT REALLY PARALLEL, BUT CONCURRENT
# NOT WORKING AS EXPECTED, IF THE FIRST AWAIT IS LONGER, THE SECOND AWAIT
# async def main():
#     get = asyncio.create_task(get_http_request())
#     post = asyncio.create_task(post_http_request("some data"))
#     await get, post
#     print(f"Get: {get.result()}, Post: {post.result()}")


# TRUE CONCURRENCY, BOTH TASKS RUN SIMULTANEOUSLY
async def main():
    get = asyncio.create_task(get_http_request())
    post = asyncio.create_task(post_http_request("some data"))
    await asyncio.gather(get, post)
    # other solution: asyncio.wait()
    print(f"Get: {get.result()}, Post: {post.result()}")


if __name__ == "__main__":
    start = perf_counter()
    asyncio.run(main())
    end = perf_counter()
    print(f"Complete: {end - start:.4f} seconds")
