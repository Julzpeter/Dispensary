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
        
  
        