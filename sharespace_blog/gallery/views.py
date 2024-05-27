from django.shortcuts import render
from .models import Product
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def product_detail(request, id):
    products = Product.objects.all()
    return render (request, "productdetails.html" , {"product": products})

def home(request):
    return HttpResponse("Hello world")