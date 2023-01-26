from typing import List

import requests
from django.core.management.base import BaseCommand

from usersapp.models import Post, User


def get_users_from_api(url: str = "https://jsonplaceholder.typicode.com/users") -> List[dict]:
    response = requests.get(url, timeout=10)
    data = response.json()
    result = [
        {
            "name": item["name"],
            "username": item["username"],
            "email": item["email"],
            "address":
                f"City: {item['address']['city']},"
                f"street: {item['address']['street']},"
                f"suite: {item['address']['suite']}.",
            "phone": item["phone"],
            "website": item["website"],
            "company": item["company"]["name"],
        }
        for item in data
    ]
    return result


def get_posts_from_api(url: str = "https://jsonplaceholder.typicode.com/posts") -> List[dict]:
    response = requests.get(url, timeout=10)
    data = response.json()
    result = [
        {
            "title": item["title"],
            "body": item["body"],
            "userId": item["userId"]
        }
        for item in data
    ]
    return result


class Command(BaseCommand):
    help = 'Fill db'

    def handle(self, *args, **options):

        #  удаление старых данных
        Post.objects.all().delete()
        User.objects.all().delete()

        # Создание пользователей
        users_json = get_users_from_api()
        users = [
            User.objects.create(
                name=user_json["name"],
                username=user_json["username"],
                email=user_json["email"],
                address=user_json["address"],
                phone=user_json["phone"],
                website=user_json["website"],
                company=user_json["company"],
            )
            for user_json in users_json
        ]

        # создание постов
        posts_json = get_posts_from_api()
        for post_json in posts_json:
            Post.objects.create(
                title=post_json['title'],
                body=post_json['body'],
                author=users[post_json['userId']-1],
            )

        print('Done')
