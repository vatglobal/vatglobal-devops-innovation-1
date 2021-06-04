import requests

url = "https://jsonplaceholder.typicode.com/posts"
pages = 100
pages_res: list = []

def loop_post_pages()-> list:
    for x in range(1, pages):
        pages_res.extend(get_request(url=f"{url}/{x}/comments"))
        print(len(pages_res))
    print(pages_res)
    print(f"Number of comments: {len(pages_res['results'])}")



def get_request(url:str="")->list:
    return requests.get(url).json()


loop_post_pages()