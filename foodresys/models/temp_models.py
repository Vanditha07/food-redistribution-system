from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
    
class TempDonorData(models.Model):
    donor_name = models.CharField(max_length=50)
    donor_phone_number = models.CharField(max_length=20)
    #food_image = serializers.ImageField()
    food_name = models.CharField(max_length=100)
    food_shelf_life = models.IntegerField() #in hours
    food_m_date = models.DateField()
    food_m_time = models.TimeField()

class TempReceiverData(models.Model):
    receiver_name = models.CharField(max_length=50)
    receiver_phone_number = models.CharField(max_length=20)