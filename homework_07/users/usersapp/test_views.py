import datetime

from django.test import TestCase

from usersapp.models import User


class TestView(TestCase):

    def test_response_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)

    def test_response_context(self):
        response = self.client.get('/')
        self.assertIn('now', response.context)
        self.assertIsInstance(response.context['now'], datetime.datetime)

    def test_user_detail(self):
        response = self.client.get('/user/99999')
        self.assertEqual(response.status_code, 404)

        user = User.objects.create(
            name='Alexander Danilevsky',
            username='a_danilevsky'
        )
        response = self.client.get(f'/user/{user.pk}')
        self.assertEqual(response.status_code, 200)

    def test_content(self):
        response = self.client.get('/')
        btn = '''<a class="nav-link"\n                       href="/users/">\n                        Users\n                    </a>'''.encode(encoding='utf-8')
        self.assertIn(btn, response.content)
