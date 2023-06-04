from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Admin

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse('<h1>About us</h1>')

#views for showing signup/login button for admin (by submit)
def adminclick_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('afterlogin')
    return render(request, 'adminclick.html')

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
    elif is_patient(request.user):
        accountapproval=models.Patient.objects.all().filter(user_id=request.user.id,status=True)
        if accountapproval:
            return redirect('patient-dashboard')
        else:
            return render(request,'hospital/patient_wait_for_approval.html')

        
  
        