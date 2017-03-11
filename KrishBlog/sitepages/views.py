from django.shortcuts import render
from .models import About

# Create your views here.

def about(request):
    about =About.objects.get(pk=1)
    return render(request,'sitepages/about.html',{"about":about})