from django.test import TestCase

from usersapp.models import User, Post


class TestUser(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            name='Alexander Danilevsky',
            username='a_danilevsky',
            company='BIOCAD'
        )

    def tearDown(self) -> None:
        del self.user
        User.objects.all().delete()

    def test_str(self):
        self.assertEqual(str(self.user), 'Alexander Danilevsky (a_danilevsky)')

    # def test_phone(self):
    #     print('phone test')
    #     # pass
    #     with self.assertRaises(Exception):
    #         User.objects.create(
    #             name='Alexander II',
    #             username='a_second',
    #             phone='11111 11111 11111 11111'
    #         )


class TestPost(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            name='Alexander Danilevsky',
            username='a_danilevsky',
            company='BIOCAD'
        )
        self.post = Post.objects.create(
            title='Test post',
            body='test body',
            author=self.user
        )

    def tearDown(self) -> None:
        Post.objects.all().delete()
        User.objects.all().delete()

    def test_str(self):
        self.assertEqual(str(self.post), 'Test post (Alexander Danilevsky)')
