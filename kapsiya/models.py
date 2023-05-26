from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Admin(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone_number = PhoneNumberField(max_length=10, null=False,blank=False,unique=True)

    

    
