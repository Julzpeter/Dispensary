from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="kapsiya-home"),
    path('about/', views.about, name="kapsiya-about"),
]