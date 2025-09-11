import asyncio


async def get_http_request():
    print("starting http request")
    await asyncio.sleep(2)
    print("http request done")
    return "response from server"


async def main():
    print(f"Get: {await get_http_request()}")


if __name__ == "__main__":
    asyncio.run(main())
