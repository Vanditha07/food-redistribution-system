from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Transaction(models.Model):
    foodID                             = models.CharField(max_length=100, blank=False, unique=True)
    food_type_item                     = models.CharField(max_length=500, blank=False)
    food_in_date                       = models.CharField(max_length=50)
    food_in_time                       = models.CharField(max_length=50)
    food_out_date                      = models.CharField(max_length=50)
    food_out_time                      = models.CharField(max_length=50)
    donor_name                         = models.CharField(max_length=100)
    donor_phone_number                 = PhoneNumberField(null=False, blank=False, unique=True)
    receiver_name                      = models.CharField(max_length=100)
    receiver_phone_number              = PhoneNumberField(null=False, blank=False, unique=True)
    #food_image                         = models.ImageField(upload_to='foodImages/')

    def __str__(self):
        return self.foodID