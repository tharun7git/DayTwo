from django import forms
from .models import StockPrice
class StockPriceForm(forms.ModelForm):
    class Meta:
        model=StockPrice
        fields='__all__'
        exclude = ['Open']
