
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',allblogs,name="allblogs"),
    path('/<slug:pk>',blogdetails,name="blogdetails")
] 