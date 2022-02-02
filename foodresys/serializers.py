from .models import TempDonorData, TempReceiverData
from rest_framework import serializers


#get data from frontend
class DonorInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempDonorData
        fields = ('__all__')

#send data to frontend
class IndexSerializer(serializers.Serializer):
    location = serializers.CharField(max_length=150)
    status = serializers.IntegerField()

#get data from frontend
class ReceiverInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TempReceiverData
        fields = ('__all__')

#show data in frontend 
class FoodInfoSerializer(serializers.Serializer):
    humidity = serializers.CharField(max_length=50)
    temperature = serializers.CharField(max_length=50)
    food_condition =  serializers.CharField(max_length=50)
    
