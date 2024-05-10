from django.urls import path
from TaygraApp import views


urlpatterns = [
   
    path('', views.home, name='home'),
    
]