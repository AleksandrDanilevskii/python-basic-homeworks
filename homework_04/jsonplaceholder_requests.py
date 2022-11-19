"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        data = await response.json()
        return data


async def get_users(url: str = USERS_DATA_URL):
    data = await fetch_json(url)
    return data


async def get_user(user_id: int, url: str = USERS_DATA_URL):
    data = await fetch_json(f"{url}/{user_id}")
    return data


async def get_posts(url: str = POSTS_DATA_URL):
    data = await fetch_json(url)
    return data


async def get_post(post_id: int, url: str = POSTS_DATA_URL):
    data = await fetch_json(f"{url}/{post_id}")
    return data

