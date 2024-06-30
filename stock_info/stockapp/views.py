# predictor/views.py
from django.shortcuts import render
from .forms import StockPriceForm
from .models import StockPrice
import joblib
import os

model_path =('STOCKPRICE__PRED.joblib')
model = joblib.load(model_path)

def predict_form(request):
    form = StockPriceForm()
    return render(request, 'predict.html', {'form': form})

def predict(request):
    if request.method == 'POST':
        form = StockPriceForm(request.POST)
        if form.is_valid():
            StockPrice = form.save(commit=False)
            features = [
                StockPrice.VWAP,
                StockPrice.Volume,
                StockPrice.Turnover,
                StockPrice.Trades,
                StockPrice.Deliverable_Volume,
                StockPrice.Deliverble,
                StockPrice.day,
                StockPrice.month,
                StockPrice.year,
                StockPrice.Prev_Close,
                StockPrice.Close,

            ]
            price = model.predict([features])[0]
            StockPrice.Open = price
            #StockPrice.save()
            return render(request, 'result.html', {'Open': price})
    else:
        form = StockPriceForm()
    return render(request, 'predict.html', {'form': form})
