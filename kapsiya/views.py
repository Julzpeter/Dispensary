from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import forms,models
from django.contrib.auth.models import Group
from django.contrib import messages

from . import models
# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse('<h1>About us</h1>')

#views for showing signup/login button for admin (by submit)
def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request, 'adminclick.html')

def admin_signup_view(request):
    form = forms.AdminSignupForm()
    if request.method == 'POST':
        form=forms.AdminSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('adminlogin')
            user = form.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)
        return HttpResponseRedirect('adminlogin')
    return render(request, 'adminsignup.html', {'form':form})

#-----------for checking user is doctor , patient or admin(by sumit)
def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()
def is_doctor(user):
    return user.groups.filter(name='DOCTOR').exists()

#after the user enters the credential the user checks whether the username and password is of admin and doctor
def afterlogin_view(request):
    if is_admin(request.user):
        return redirect('admin-dashboard')
    elif is_doctor(request.user):
        accountapproval=models.Doctor.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('doctor-dashboard')
        else:
            return render(request,'hospital/doctor_wait_for_approval.html')
    

        
  
        