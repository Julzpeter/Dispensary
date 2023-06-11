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

class DoctorUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        
class DoctorForm(forms.ModelForm):
    class Meta:
        model=models.Doctor
        fields=['address','mobile','department','status','profile_pic']