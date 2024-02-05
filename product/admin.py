from django.contrib import admin
from .models import *
# Register your models here.
class productiteminline(admin.StackedInline):
    model = productitem
    extra = 1  # Set the number of empty forms to display

@admin.register(products)
class CoursesDetailsAdmin(admin.ModelAdmin):
    inlines = [productiteminline]


admin.site.register(productcontact)