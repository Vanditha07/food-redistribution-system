from django.shortcuts import render
import pyrebase
from .models import Transaction, Authority

firebaseConfig = {
    'apiKey': "AIzaSyCn1fWSoBz4pPzso6Ejyky-d-7gKZAqhks",
    'authDomain': "food-redistribution-system.firebaseapp.com",
    'databaseURL': "https://food-redistribution-system-default-rtdb.firebaseio.com",
    'projectId': "food-redistribution-system",
    'storageBucket': "food-redistribution-system.appspot.com",
    'messagingSenderId': "984251987266",
    'appId': "1:984251987266:web:7f8a3069bff9389214c4db"
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()
