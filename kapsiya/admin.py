from django.contrib import admin
from .models import Admin, Doctor

# Register your models here.
class Admin(admin.ModelAdmin):
    pass
admin.site.register(Admin, Admin)

class Doctor(admin.ModelAdmin):
    pass
admin.site.register(Doctor,Doctor)
