from django.shortcuts import render
from .models import *
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.


def allbrands(request):
    brands = brandsitem.objects.all()
    return render(request,'brands/allbrand.html',{'brands':brands})



def brandsview(request,pk):
    brands = brandsitem.objects.filter(slug=pk)
    if brands:
        brandsinstance = brandsitem.objects.get(slug=pk)
        brandfaqs = brandfaq.objects.filter(brand=brandsinstance)
        # contact form
        storage = messages.get_messages(request)
        storage.used = True
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            Phone = request.POST.get('Phone')
            brand = brandsinstance
            message = request.POST.get('message')
            if name and email and Phone and brand and message:
                brandcontact.objects.create(name=name,email=email,phono=Phone,brand=brand,msg=message)
                messages.success(request, 'Request Submited')
                current_url = request.build_absolute_uri()
                return HttpResponseRedirect(current_url)
        # end contact form

        context = {
            'brands':brands,
            "brandfaqs":brandfaqs
        }
        return render(request,'brands/brandview.html',context)
    else:
        return render(request, '404.html', status=404)


