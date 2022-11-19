"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import aiohttp

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"
USERS_DATA_FIELDS = ['id', 'name', 'username', 'email']


async def fetch_json(url: str):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        data = await response.json()
        return data


async def get_users(url: str = USERS_DATA_URL, fields: list[str] | None = USERS_DATA_FIELDS):
    data = await fetch_json(url)
    if fields:
        return [{field: user[field] for field in fields} for user in data]
    return data


async def get_user(user_id: int, url: str = USERS_DATA_URL, fields: list[str] | None = USERS_DATA_FIELDS):
    data = await fetch_json(f"{url}/{user_id}")
    if fields:
        return {field: data[field] for field in fields}
    return data


async def get_posts(url: str = POSTS_DATA_URL):
    data = await fetch_json(url)
    return data


async def get_post(post_id: int, url: str = POSTS_DATA_URL):
    data = await get_posts(f"{url}/{post_id}")
    return data

