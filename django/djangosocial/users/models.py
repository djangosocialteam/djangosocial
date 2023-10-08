"""Custom user model."""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model that may eventually be extended."""

    pass
