from django.contrib import admin
from .models import *
# Register your models here.
class productiteminline(admin.StackedInline):
    model = productitem
    extra = 1  # Set the number of empty forms to display

@admin.register(products)
class CoursesDetailsAdmin(admin.ModelAdmin):
    inlines = [productiteminline]


class contactmodel(admin.ModelAdmin):
     list_display = ('name', 'phono', 'product','date')
     list_filter = ('product',)
     search_fields = ('name', 'product')



admin.site.register(productcontact,contactmodel)