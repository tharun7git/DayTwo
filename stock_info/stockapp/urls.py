from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [

    path('', views.predict_form, name='predict_form'),
    path('predict/', views.predict, name='predict'),
]
