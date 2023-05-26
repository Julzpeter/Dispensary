from django.db import models
from phone_field import PhoneField

# Create your models here.
class Admin(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.PasswordField(max_length=50)
    phonenumber = models.PhoneField(max_length=10, null=False,blank=False,unique=True)
    
