from django.shortcuts import render
from .models import *
# Create your views here.


def allblogs(request):
    blogs = Blogpost.objects.all()
    
    context = {
        'blogs' : blogs
    }

    return render(request,'blog/allblog.html',context)

def blogdetails(request, pk):
    blogdetail = Blogpost.objects.filter(slug = pk)
    if blogdetail:
        blogs = Blogpost.objects.all()
        tags = Tag.objects.all()
        context= {
            'blogdetail':blogdetail,
            'blogs' : blogs,
            "tags":tags
        }
        return render(request,'blog/blogdetails.html',context)
    else:
        return render(request, '404.html', status=404)