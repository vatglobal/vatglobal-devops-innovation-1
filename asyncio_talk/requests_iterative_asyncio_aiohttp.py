import asyncio
import time

import requests
import aiohttp

url = "https://jsonplaceholder.typicode.com/posts"
pages = 100
pages_res: list = []

async def loop_post_pages()-> list:
    asyncio_tasks = []
    for x in range(1,pages):
        asyncio_tasks.append(get_request(url=f"{url}/{x}/comments"))
    print(len(pages_res))
    return asyncio_tasks

# blocking courotine
async def get_request(url:str="")->list:
    # Blocking library
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            resp = await resp.json()
            return resp

async def asyncio_gather()->list:
    tasks = list(await loop_post_pages())

    results = await asyncio.gather(*tasks)
    for x in results:
        pages_res.extend(x)
    print(pages_res)
    print(f"Number of comments: {len(pages_res)}")

    return pages_res

begin = time.time()
asyncio.run(asyncio_gather())
end = time.time()

print("Time taken to execute the \
function is", end - begin)