from django.shortcuts import render
from . import models
# Create your views here.

def product(request):
    products = models.Product.objects.all()
    return render(request, 'product_list.html', {'products': products})