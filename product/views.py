from django.shortcuts import render
from .models import Product, ProductImages

def productlist(request):
    productlist = Product.objects.all()
    context = {
        'product_list' : productlist
    }
    return render(request, 'product/product_list.html', context)


def productdetails(request, slug):
    productdetails = Product.objects.get(slug=slug)
    productimages = ProductImages.objects.filter(product=productdetails)

    context = {
        'product_details' : productdetails,
        'product_images' : productimages
    }
    return render(request, 'product/product_details.html', context)


def index(request):
    return render(request,'product/index.html')