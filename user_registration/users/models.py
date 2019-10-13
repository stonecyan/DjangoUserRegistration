from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    website = models.URLField(max_length=150, default='')
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'website']
