
from django.shortcuts import render,redirect
from django.urls import path
from . import views
from .models import Book
from .forms import BookForm
def home(request):
    return render(request,'home.html')
def book_data(request):
    books=Book.objects.all()
    return render(request,'book_data.html',{'books':books})

def addbook(request):
    if(request.method=='POST'):
        form=BookForm(request.POST)
        if(form.is_valid):
            form.save()
            return redirect(book_data)
    else:
        form=BookForm()
        return render(request,'addbook.html',{'form':form})