
from django.shortcuts import render
from django.urls import path
from . import views
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
