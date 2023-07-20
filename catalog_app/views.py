from django.shortcuts import render

from catalog_app.models import Product


# Create your views here.


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Каталог'
    }
    return render(request, 'catalog_app/home.html', context)


def product(request):
    context = {
        'title': 'Продукт'
    }

    return render(request, 'catalog_app/product.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')

    return render(request, 'catalog_app/contacts.html', context)
