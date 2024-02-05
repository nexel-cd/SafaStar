
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
 path('',allbrands,name="allbrands"),
 path('<slug:pk>',brandsview,name="brandsview")
] 