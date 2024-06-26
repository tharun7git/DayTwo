from django.db import models

# Create your models here.
class Book(models.Model):
    Bookid=models.AutoField(primary_key=True)
    Bookname=models.CharField(max_length=200)
    Author=models.CharField(max_length=200)
    Rack=models.CharField(max_length=10)
def __str__(self):
    return self.Bookname