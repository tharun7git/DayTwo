from django.db import models

# Create your models here.
class Clg(models.Model):
    cid=models.AutoField(primary_key=True)
    Cname=models.CharField(max_length=200)
    Cadress=models.CharField(max_length=200)
    Cphno=models.CharField(max_length=10)
def __str__(self):
    return self.Cname