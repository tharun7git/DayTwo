from django.db import models

# Create your models here.
class ModelU(models.Model):
    user_id=models.AutoField(primary_key=True)
    invoice_date=models.DateField()
    job_card_date=models.DateField()
    business_partner_name=models.CharField(max_length=200)
    vehicle_no=models.IntegerField()
    vehicle_model=models.CharField(max_length=200)
    current_km_reading=models.IntegerField()
    invoice_line_text=models.CharField(max_length=1000)