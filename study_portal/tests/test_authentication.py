from django.test import TestCase
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()


class SigninTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='ivan', password='test', email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='ivan', password='test')
        self.assertTrue(user.is_authenticated)

    def test_incorrect_username(self):
        user = authenticate(username='qwe', password='test')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_incorrect_password(self):
        user = authenticate(username='ivan', password='qwe')
        self.assertFalse(user is not None and user.is_authenticated)

