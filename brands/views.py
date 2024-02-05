from django.shortcuts import render
from .models import *
# Create your views here.


def brandsview(request,pk):
    brands = brandsitem.objects.filter(slug=pk)
    # if request.method == "POST":
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     Phone = request.POST.get('Phone')
    #     name = request.POST.get('name')
    context = {
        'brands':brands
    }
    return render(request,'brands/brandview.html',context)