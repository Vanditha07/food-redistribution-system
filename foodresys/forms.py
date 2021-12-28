from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from foodresys.models import Authority

class NewUserForm(UserCreationForm):
	auth_name                = forms.CharField(required=True)
    auth_phone_number        = PhoneNumberField(
        widget = PhoneNumberPrefixWidget()
    ) 

	class Meta:
		model    = Authority
		fields   = ("username", "auth_name", "auth_phone_number", "password1", "password2")


    