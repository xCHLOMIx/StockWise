from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class User(AbstractUser):
    username = models.CharField(max_length=50)
    phonenumber = PhoneNumberField(null = False, unique = True)

    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    