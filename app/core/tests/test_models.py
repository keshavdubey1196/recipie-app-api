"""
Tests for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models"""

    def test_creatae_user_with_email_successfull(self):
        """Test creating a user with an email is successfull"""
        email = "test@em.com"
        password = "testda234"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
