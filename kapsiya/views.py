from django.shortcuts import render
from django.http import HttpResponse
from .models import Admin

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse('<h1>About us</h1>')

def adminclick_view(request):
        
  
        return HttpResponse('<h1>Hello Admin</h1>')