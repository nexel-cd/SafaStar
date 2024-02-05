from django.shortcuts import render
from .models import *
# Create your views here.
def productviews(request,pk):
    product = products.objects.filter(slug=pk)
    productget = products.objects.get(slug=pk)
    productitems = productitem.objects.filter(product=productget.id)
    context = {
        "product":product,
        "productitems":productitems
    }
    return render(request,'product/productview.html',context)