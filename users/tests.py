from django.test import TestCase
from django.contrib.auth.models import User


class UserTestCase(TestCase):
    def test_user(self):
        username = "buzz"
        password = "timallen"
        u = User(username=username)
        u.set_password(password)
        u.save()

        self.assertEqual(u.username, username)
        self.assertEqual(u.check_password(password))
