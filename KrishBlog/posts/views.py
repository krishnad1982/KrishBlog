from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def home(request):
    posts=Post.objects.order_by("-pub_date")
    return render(request,"posts/home.html",{"posts":posts})

def postdetails(request,post_id):
    try:
        post=Post.objects.get(id=post_id)
        return render(request,"posts/postdetails.html",{"post":post})
    except Exception:
        return HttpResponse("no posts found")
    

