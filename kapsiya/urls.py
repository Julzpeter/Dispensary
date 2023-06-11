from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.home, name="kapsiya-home"),
    path('about/', views.about, name="kapsiya-about"),
    path('adminclick/', views.adminclick_view, name="kapsiya-admin"),

    path('adminlogin/', LoginView.as_view(template_name="adminlogin.html")),

    

    path('afterlogin', views.afterlogin_view, name='afterlogin'),
]