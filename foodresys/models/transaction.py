from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Transaction(models.Model):
    food_code                          = models.CharField(max_length=100, blank=False, unique=True)
    food_type                          = models.CharField(max_length=500, blank=False)
    food_in_date                       = models.DateField(auto_now_add=False, auto_now=False, blank=False)
    food_in_time                       = models.TimeField(auto_now=False, auto_now_add=False, blank=False)
    food_out_date                      = models.DateField(auto_now_add=False, auto_now=False, blank=False)
    food_out_time                      = models.TimeField(auto_now=False, auto_now_add=False, blank=False)
    donor_name                         = models.CharField(max_length=100)
    donor_phone_number                 = PhoneNumberField(null=False, blank=False, unique=True)
    receiver_name                      = models.CharField(max_length=100)
    receiver_phone_number              = PhoneNumberField(null=False, blank=False, unique=True)
   