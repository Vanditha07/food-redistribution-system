from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Consumer(models.Model):
    consumer_name                      = models.CharField(max_length=200, blank=False)
    consumer_phone_number              = PhoneNumberField(null=False, blank=False, unique=True)
    consumer_emailID                   = models.EmailField(max_length=200, blank=False )

    def __str__(self):
        return self.consumer_name