from typing import List

import requests

TEST_USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"


def get_users_from_api(url: str = TEST_USERS_DATA_URL) -> List[dict]:
    response = requests.get(url)
    data = response.json()
    result = [
        {
            'id': item['id'],
            'name': item['name'],
            'username': item['username'],
            'email': item['email'],
            'address': f"City: {item['address']['city']}, street: {item['address']['street']}, suite: {item['address']['suite']}.",
            'phone': item['phone'],
            'website': item['website'],
            'company': item['company']['name'],
        } for item in data]
    return result
