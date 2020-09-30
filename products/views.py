from django.shortcuts import render
from products.models import FarmProduct

# Create your views here.
all_products = FarmProduct.objects.all

def homepage(request):
    return render(request, 'FarmBase.html',)

def shop(request):
	return render(request, 'Shop.html',  {'all':all_products})

def comingsoon(request):
	return render(request, 'ComingSoon.html')
