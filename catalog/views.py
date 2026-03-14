from django.http import HttpResponse
from django.shortcuts import render
from catalog.models import Product

# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {
       'products': products
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse(f'Спасибо, {name}! Ваше сообщение получено.')

    return render(request, 'catalog/contacts.html')


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'catalog/product_detail.html', context)