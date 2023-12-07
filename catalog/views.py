from django.shortcuts import render

from catalog.models import Product


def home(request):
    catalog_list = Product.objects.all()
    context = {
        'object_list' : catalog_list,
    }
    return render(request, 'main/home.html', context)

def product(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
    }
    return render(request, 'main/product.html', context)

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'main/contacts.html')
