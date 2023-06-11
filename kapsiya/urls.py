from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='kapsiya-home'),
    path('adminclick/', views.adminclick_view, name='kapsiya-admin'),
    path('adminsignup/', views.admin_signup_view, name='adminsignup'),
    path('adminlogin/', views.admin_login, name='adminlogin'),
    

   

    

    path('afterlogin', views.afterlogin_view, name='afterlogin'),
]