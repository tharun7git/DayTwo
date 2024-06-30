
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import path
from . import views
from .forms import StudentForm
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

def addstudent(request):
    if(request.method=='POST'):
        form=StudentForm(request.POST)
        if(form.is_valid):
            form.save()
            return redirect(student_data)
    else:
        form=StudentForm()
        return render(request,'add_data.html',{'form':form})
    
