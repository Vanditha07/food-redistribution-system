from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Authority, Transaction, Consumer, TempReceiverData, TempDonorData

class CustomTransaction(admin.ModelAdmin):
    model = Transaction
    list_display = ('foodID', 'food_type_item', 'food_in_date', 'food_in_time', 'food_out_date', 'food_out_time', 'donor_name', 'donor_phone_number', 'receiver_name', 'receiver_phone_number')

class CustomConsumer(admin.ModelAdmin):
    model = Consumer
    list_display = ('consumer_name', 'consumer_phone_number', 'consumer_emailID')


# Register your models here.
admin.site.register(Authority, UserAdmin)
admin.site.register(Transaction, CustomTransaction)
admin.site.register(Consumer, CustomConsumer)
admin.site.register(TempDonorData)
admin.site.register(TempReceiverData)