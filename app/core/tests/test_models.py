from django.test import TestCase
from django.contrib.auth import get_user_model


class modelTests(TestCase):
    """docstring for modelTests."""

    def test_create_user_with_email_successful(self):
        email = 'sid@gmail.com'
        password = 'sid123'
        user = get_user_model().objects.create_user(
        email = email,
        password = password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'sid@gmail.com'
        user = get_user_model().objects.create_user(email, 'sid123')

        self.assertEqual(user.email, email.lower())
