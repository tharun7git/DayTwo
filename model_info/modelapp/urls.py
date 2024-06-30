from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    path('',views.home),
    path('model_data',views.model_data,name='model_data'),
]