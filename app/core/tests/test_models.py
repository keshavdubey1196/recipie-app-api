"""
Tests for models
"""
from decimal import Decimal
from core import models

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

    def test_new_user_email_normalized(self):
        """Test email is normalized for new users"""
        sample_emails = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, "sample@123")
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without an email raises a value error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "sample@123")

    def test_create_superuser(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            "test@example.com",
            "test@123",
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipie(self):
        """Test creating a recipie is successful"""
        user = get_user_model().objects.create_user(
            "test@example.com",
            "testpass123",
        )
        recipie = models.Recipe.objects.create(
            user=user,
            title="Same recipe name",
            time_minutes=5,
            price=Decimal("5.58"),
            description="Sample recipe description",
        )

        self.assertEqual(str(recipie), recipie.title)
