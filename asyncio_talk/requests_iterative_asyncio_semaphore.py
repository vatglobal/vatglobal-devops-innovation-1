#     results = await asyncio.gather(*tasks)

# sem = asyncio.Semaphore(5)
# async with sem:
#     results = await asyncio.gather(*tasks)
import asyncio
import time

import requests

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
    return requests.get(url).json()

async def asyncio_gather()->list:
    tasks = list(await loop_post_pages())

    sem = asyncio.Semaphore(10)
    async with sem:
        results = await asyncio.gather(*tasks)
    for x in results:
        pages_res.append(x)
    print(pages_res)
    print(f"Number of comments: {len(pages_res)}")

    return pages_res

begin = time.time()
asyncio.run(asyncio_gather())
end = time.time()

print("Time taken to execute the \
function is", end - begin)