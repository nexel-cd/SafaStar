from django.contrib import admin
from .models import *




# Register your models here.
class contactmodel(admin.ModelAdmin):
     list_display = ('name', 'phono','date')

     search_fields = ('name',)

admin.site.register(contact,contactmodel)
admin.site.register(ads)

