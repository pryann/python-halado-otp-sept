import requests


def get_posts():
    try:
        url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(url)
        if response.ok:
            return response.json()
        else:
            return []
    except requests.RequestException:
        return None


if __name__ == "__main__":
    posts = get_posts()
    print(posts)
    print(type(posts))
