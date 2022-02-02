from django.shortcuts import render
import pyrebase
from django.views.decorators.csrf import csrf_exempt

from foodresys.models.temp_models import TempReceiverData, TempDonorData
from .models import Transaction, Authority
from .serializers import DonorInfoSerializer, IndexSerializer, FoodInfoSerializer, ReceiverInfoSerializer
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .extras import IndexViewData, FoodInfoData
import string
import random
from datetime import date, datetime
from rest_framework import status

firebaseConfig = {
    'apiKey': "AIzaSyCn1fWSoBz4pPzso6Ejyky-d-7gKZAqhks",
    'authDomain': "food-redistribution-system.firebaseapp.com",
    'databaseURL': "https://food-redistribution-system-default-rtdb.firebaseio.com",
    'projectId': "food-redistribution-system",
    'storageBucket': "food-redistribution-system.appspot.com",
    'messagingSenderId': "984251987266",
    'appId': "1:984251987266:web:7f8a3069bff9389214c4db"
}

firebase = pyrebase.initialize_app(firebaseConfig)
authe = firebase.auth()
database = firebase.database()

@api_view(['GET'])
def IndexView(request):
    status = database.child("Condition").get().val()
    location = database.child("ESP32Info").child("Location").get().val()
    data_obj = IndexViewData(location, status)
    serializer_class = IndexSerializer(data_obj)
    return Response(serializer_class.data)

@api_view(['GET'])
def FoodInfoView(request):
    humidity = database.child("ESP32Info").child("Humidity").get().val()
    temperature = database.child("ESP32Info").child("Temperature").get().val()
    mq2output = database.child("ESP32Info").child("MQ2Output").get().val()
    if (mq2output == "No gas"):
        food_condition = "Not Spoiled"
    else: 
        food_condition = "Spoiled"
    info_obj = FoodInfoData(humidity, temperature, food_condition)
    serializer_class = FoodInfoSerializer(info_obj)
    return Response(serializer_class.data)


class DonorInfoView(APIView):
    @csrf_exempt
    def post(self, request):
        serializer = DonorInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            donor_name = string(TempDonorData.objects.values_list('donor_name'))
            donor_phone_number = string(TempDonorData.objects.values_list('donor_phone_number'))
            food_name = string(TempDonorData.objects.values_list('food_name'))
            food_shelf_life = int(TempDonorData.objects.values_list('food_shelf_life'))
            food_m_date = string(TempDonorData.objects.values_list('food_m_date'))
            food_m_time = string(TempDonorData.objects.values_list('food_m_time'))

            condition = 1
            database.child("Condition").set(condition)
            database.child("ESP32Info").child("DonorName").set(donor_name)
            database.child("ESP32Info").child("DonorPhoneNumber").set(donor_phone_number)
            food_id = 'PV' + ''.join(random.choices(string.digits, k = 4))
            database.child("ESP32Info").child("FoodID").set(food_id)
            #database.child("ESP32Info").child("FoodImage").set(food_image)
            in_date = date.today()
            in_time = datetime.now().strftime("%H:%M:%S")
            database.child("ESP32Info").child("FoodIn_Info").child("InDate").set(in_date)
            database.child("ESP32Info").child("FoodIn_Info").child("InTime").set(in_time)
            database.child("ESP32Info").child("FoodType").child("Item").set(food_name)
            database.child("ESP32Info").child("FoodType").child("Manufacture_Info").child("Mdate").set(food_m_date)
            database.child("ESP32Info").child("FoodType").child("Manufacture_Info").child("Mtime").set(food_m_time)
            database.child("ESP32Info").child("FoodType").child("ShelfLife").set(food_shelf_life)
            TempDonorData.objects.delete()

            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        
class ReceiverInfoView(APIView):
    @csrf_exempt
    def post(self, request):
        serializer = ReceiverInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            food_ID = database.child("UserInput").child("FoodID").get().val()
            food_type_item = database.child("UserInput").child("FoodType").child("Item").get().val()
            food_in_date = database.child("UserInput").child("FoodIn_Info").child("InDate").get().val()
            food_in_time = database.child("UserInput").child("FoodIn_Info").child("InTime").get().val()
            food_out_date = date.today()
            food_out_time = datetime.now().strftime("%H:%M:%S")
            donor_name = database.child("UserInput").child("DonorName").get().val()
            donor_phone_number = database.child("UserInput").child("DonorPhoneNumber").get().val()
            receiver_name = string(TempReceiverData.objects.values_list('receiver_name'))
            receiver_phone_number = string(TempReceiverData.values_list('receiver_phone_number'))
            TempReceiverData.objects.delete()
            #food_image = database.child("UserInput").child("FoodImage").get().val()
            transaction = Transaction(foodID=food_ID, food_type_item=food_type_item, food_in_date=food_in_date, food_in_time=food_in_time, food_out_date=food_out_date, food_out_time=food_out_time, donor_name=donor_name, donor_phone_number=donor_phone_number, receiver_name=receiver_name, receiver_phone_number=receiver_phone_number)#, #food_image=food_image)
            transaction.save()

            condition = 0 
            data = 'Null'
            database.child("Condition").set(condition)
            database.child("ESP32Info").child("Humidity").set(data)
            database.child("ESP32Info").child("Location").set(data)
            database.child("ESP32Info").child("Temperature").set(data)
            database.child("UserInput").child("DonorName").set(data)
            database.child("UserInput").child("DonorPhoneNumber").set(data)
            database.child("UserInput").child("FoodID").set(data)
            #database.child("UserInput").child("FoodImage").remove()
            database.child("UserInput").child("Foodln_Info").child("InDate").SET(data)
            database.child("UserInput").child("Foodln_Info").child("InTime").SET(data)
            database.child("UserInput").child("FoodType").child("Item").set(data)
            database.child("UserInput").child("FoodType").child("Manufacture_Info").child("MDate").set(data)
            database.child("UserInput").child("FoodType").child("Manufacture_Info").child("Mtime").set(data)
            database.child("UserInput").child("FoodType").child("ShelfLife").set(data)

            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


