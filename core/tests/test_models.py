from django.test import TestCase
from django.contrib.auth import get_user_model

class TestModels(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating a new user with email is successful"""
        email = "onagoruwam@gmail.com"
        password = "test123"
        user = get_user_model().objects.create_user(
            email=email, 
            password=password)
        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))    