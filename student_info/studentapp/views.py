
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from . import views
from .models import Student
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def add(request,a,b):
    c=a+b
    return HttpResponse("the addition is"+str(c))
def student_data(request):
    students=Student.objects.all()
    return render(request,'student_data.html',{'students':students})