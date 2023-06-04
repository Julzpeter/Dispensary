from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="kapsiya-home"),
    path('about/', views.about, name="kapsiya-about"),
    path('adminclick/', views.adminclick_view, name="kapsiya-admin"),

    path('afterlogin', views.afterlogin, name='afterlogin'),
]