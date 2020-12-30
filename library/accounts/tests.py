"""module for testing accounts app"""
from django.test import TestCase

from .forms import SignUpForm
from .models import Profile


class AccountsTestCase(TestCase):
    """class with tests regarding accounts app"""

    def test_can_create_instance_of_signup_form(self):
        """signUpForm can be instantiated"""
        form = SignUpForm()
        self.assertIsInstance(form, SignUpForm)

    def test_can_create_instance_of_profile_model(self):
        """profile model can be instantiated"""
        profile = Profile()
        self.assertIsInstance(profile, Profile)
