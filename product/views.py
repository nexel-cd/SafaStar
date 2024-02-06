from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
def productviews(request,pk):
    product = products.objects.filter(slug=pk)
    if product:
        productget = products.objects.get(slug=pk)
        productitems = productitem.objects.filter(product=productget.id)
        storage = messages.get_messages(request)
        storage.used = True
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            Phone = request.POST.get('Phone')
            brand = productget
            message = request.POST.get('message')
            if name and email and Phone and brand and message:
                productcontact.objects.create(name=name,email=email,phono=Phone,product=brand,msg=message)
                messages.success(request, 'Request Submited')
                current_url = request.build_absolute_uri()
                return HttpResponseRedirect(current_url)
        context = {
            "product":product,
            "productitems":productitems
        }
        return render(request,'product/productview.html',context)
    else:
        return render(request, '404.html', status=404)