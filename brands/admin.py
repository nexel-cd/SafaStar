from django.contrib import admin
from .models import *
# Register your models here.

class contactmodel(admin.ModelAdmin):
     list_display = ('name', 'phono', 'brand','date')
     list_filter = ('brand',)
     search_fields = ('name', 'brand')


admin.site.register(brandsitem)
admin.site.register(brandcontact,contactmodel)
admin.site.register(brandfaq)


