from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('bb',views.book_data),
    path('addbook',views.addbook,name='AddBook')
]