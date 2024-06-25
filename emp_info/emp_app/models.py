from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    sal=models.CharField(max_length=10)
    def __str__(self):
        return self.name