from django.shortcuts import render
from django.urls import path
from . import views
from .models import ModelU
def home(request):
    return render(request,'home.html')
def model_data(request):
    models=ModelU.objects.all()
    return render(request,'model_data.html',{'models':models})