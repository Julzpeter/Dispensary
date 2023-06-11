from django import forms
from django.contrib.auth.models import User
from . import models

#for admin signup
class AdminSignupForm(forms.ModelForm):
    class Meta:
        model=User
        """
         help_texts = {
            'username': None,
        }
        """
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        
class AuthenticationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username', 'password']
        widgets = {
            'password': forms.PasswordInput()

        }