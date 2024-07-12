from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    product_instance = Product.objects.all()
    # print(product_instance.values())
    return render(request, 'index.html', {'products': product_instance})


def shop(request):
    return render(request, 'shop.html')
