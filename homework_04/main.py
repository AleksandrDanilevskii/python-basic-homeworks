"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
from typing import List

from sqlalchemy.ext.asyncio import AsyncEngine

from homework_04.models import async_engine, Base, User, async_session, AsyncSession, Post, Session
from jsonplaceholder_requests import (
    get_users,
    get_posts,
)


async def create_tables(engine: AsyncEngine, metadata):
    async with engine.begin() as conn:
        await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)

    print('tables created')


async def create_users(session: AsyncSession, users_json: List[dict]) -> list[User]:

    users = [
        User(id=user_json['id'], name=user_json['name'], username=user_json['username'], email=user_json['email'])
        for user_json in users_json
    ]
    session.add_all(users)
    await session.commit()
    print("created users", users)

    return users


async def create_posts(session: AsyncSession, posts_json: List[dict]) -> list[Post]:

    posts = [
        Post(id=post_json['id'], title=post_json['title'], body=post_json['body'], user_id=post_json['userId'])
        for post_json in posts_json
    ]
    session.add_all(posts)
    await session.commit()
    print("created posts", posts)

    return posts


async def async_main():
    # удаляем/создаем чистенькие таблицы
    await create_tables(engine=async_engine, metadata=Base.metadata)

    # получаем данные
    users_data: List[dict]
    posts_data: List[dict]
    users_data, posts_data = await asyncio.gather(
        get_users(),
        get_posts(),
    )

    # записываем данные в DB
    async with Session() as session:
        await create_users(session=session, users_json=users_data)
        await create_posts(session=session, posts_json=posts_data)


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
