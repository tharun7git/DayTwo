from django.db import models

# Create your models here.
class StockPrice(models.Model):
    Open = models.FloatField()
    VWAP = models.FloatField()
    Volume = models.FloatField()
    Turnover = models.FloatField()
    Trades = models.FloatField()
    Deliverable_Volume = models.FloatField()
    Deliverble = models.FloatField()
    day = models.FloatField()
    month = models.FloatField()
    year = models.FloatField()
    Prev_Close = models.FloatField()
    Close=models.FloatField()
