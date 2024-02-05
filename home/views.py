from django.shortcuts import render
from blog.models import Blogpost
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
    return render(request,'contactus.html')