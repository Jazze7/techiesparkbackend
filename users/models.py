from django.db import models
from django.contrib.auth.models import AbstractUser
from users.manager import UserManager


class User(AbstractUser):
    username=None
    # name=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=15,unique=True)
    is_verified = models.BooleanField(default=False)
    otp=models.CharField(max_length=6)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS =[]
    objects=UserManager()