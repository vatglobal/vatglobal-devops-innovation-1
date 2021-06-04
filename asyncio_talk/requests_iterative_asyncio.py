import asyncio

import requests

url = "https://jsonplaceholder.typicode.com/posts"
pages = 100
pages_res: dict = {'results': []}



async def loop_post_pages()-> list:
    asyncio_tasks = []
    for x in range(1,pages):
        asyncio_tasks.append(get_request(url=f"{url}/{x}/comments"))
    print(len(pages_res))
    return asyncio_tasks


async def get_request(url:str="")->list:
    return {'res': requests.get(url).json()}

async def asyncio_gather()->list:
    tasks = list(await loop_post_pages())

    results = await asyncio.gather(*tasks)
    for x in results:
        pages_res['results'].extend(x['res'])
    print(pages_res['results'])
    print(f"Number of comments: {len(pages_res['results'])}")

    return pages_res

asyncio.run(asyncio_gather())