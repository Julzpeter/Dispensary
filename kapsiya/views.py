from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import forms,models
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm #add this


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
    if request.method == 'POST':
        form=forms.AdminSignupForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            messages.success(request,"egistration Successful.")
            return redirect("adminlogin")
        messages.error(request, "Unsuccessful registration. Invalid Information.")
        return HttpResponseRedirect('adminlogin')
    else:
        form = forms.AdminSignupForm()      
    return render(request, 'adminsignup.html', {'form':form})

def admin_login(request):
    if request.method == "POST":
        form = forms.AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request,f"You are now logged in as{username}.")
                return redirect("admin-dashboard")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")

    form = AuthenticationForm()
    return render(request, 'adminlogin.html', context={"login_form":form})
                    
                
		    

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
    

        
  
        