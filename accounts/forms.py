from django import forms
from .models import User

class loginForm(forms.ModelForm):

        class Meta:
            model = User
            fields = ['email', 'password']
            widgets = {
                'password': forms.PasswordInput(),
            }
