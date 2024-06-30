
from django.shortcuts import render,redirect,get_object_or_404
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

def deletebook(request,pk): 
    book=get_object_or_404(Book,pk=pk)
    book.delete()
    return redirect(book_data)

def editbook(request,pk):
    book=get_object_or_404(Book,pk=pk)
    if(request.method=='POST'):
        form=BookForm(request.POST,instance=book)
        if(form.is_valid):
            book=form.save()
            return redirect(book_data)
    else:
        form=BookForm(instance=book)
        return render(request,'addbook.html',{'form':form})