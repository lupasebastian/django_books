"""models to be used in accounts app"""

from django.contrib.auth.models import User
from django.db.models import Model, OneToOneField, CASCADE, TextField


class Profile(Model):
    """class for creating Profile objects while signing up"""
    user = OneToOneField(User, on_delete=CASCADE)
    information = TextField()
