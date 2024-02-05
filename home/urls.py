
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   path('',home,name="home"),
   path('about',aboutcompany,name="about"),
   path('Contactus',Contactus,name="Contactus")
] 