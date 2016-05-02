from django import forms
from .models import Contacts

class addContact(forms.ModelForm):
     class Meta:
         model= Contacts
         fields= ['company_name', 'first_name', 'last_name', 'phone', 'email']
