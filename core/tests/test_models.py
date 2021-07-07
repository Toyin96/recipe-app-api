from core.models import User
from django import test
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

    def test_new_user_email_normalize(self):
        """test the email for a new user is normalize"""
        email = "onagoruwam@GMAIL.COM"
        user = get_user_model().objects.create_user(email, "test123")
        self.assertEquals(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating user with no email raises error""" 
        with self.assertRaises(ValueError):
            password = 'test123'
            get_user_model().objects.create_user(email=None, password=password)
          
    def test_create_super_user(self):
        """Test creating a super user"""
        user = get_user_model().objects.create_superuser(
            "onagoruwam@gmail.com",
            "super123"
        )  

        self.assertTrue(User.is_superuser)