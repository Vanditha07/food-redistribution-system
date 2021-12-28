from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Authority(AbstractUser):
    username                       = models.CharField(max_length=50, unique=True)
    auth_name                      = models.CharField(max_length=100)
    auth_phone_number              = PhoneNumberField(null=False, blank=False, unique=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['auth_name', 'auth_phone_number']

    def __str__(self):
        return self.username

    