from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


# Create your models here.


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    phone_number = PhoneNumberField(max_length=13, null=False,blank=False,unique=True)

    @property
    def get_name(self):
        return self.user.first_name+ "" +self.user.last_name 
    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return "{} ({})".format(self.user.first_name) 

    
