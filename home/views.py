from django.shortcuts import render
from blog.models import Blogpost
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import *
# Create your views here.


def home(request):
    blog = Blogpost.objects.all()
    context = {
        "blog":blog
    }
    return render(request,'index.html',context)



def aboutcompany(request):
    return render(request,'about.html')



def Contactus(request):
    storage = messages.get_messages(request)
    storage.used = True
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        Phone = request.POST.get('Phone')
        message = request.POST.get('message')
        if name and email and Phone and message:
            contact.objects.create(name=name,email=email,phono=Phone,msg=message)
            messages.success(request, 'Request Submited')
            current_url = request.build_absolute_uri()
            return HttpResponseRedirect(current_url)
    return render(request,'contactus.html')




# custom 404 view
def custom_404(request, exception):
    return render(request, '404.html', status=404)