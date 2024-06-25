
from django.shortcuts import render
from django.urls import path
from . import views
from .models import Clg
def home(request):
    return render(request,'home.html')
def clg_data(request):
    clgs=Clg.objects.all()
    return render(request,'clg_data.html',{'clgs':clgs})
