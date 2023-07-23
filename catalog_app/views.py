from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from catalog_app.models import Product, Category


# Create your views here.


def home(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list,
        'title': 'Продукты'
    }
    return render(request, 'catalog_app/index.html', context)


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категория продуктов'
    }


# def product(request, pk):
#     context = {
#         'object_list': Product.objects.filter(pk=pk),
#         'title': 'Продукт'
#     }
#
#     return render(request, 'catalog_app/product_form.html', context)

class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        contex_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        contex_data['category_pk'] = category_item.pk
        contex_data['title'] = f'Продукты категории - все наши категории {category_item.name}'

        return contex_data


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


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'desc', 'price', 'category', 'image')
    success_url = reverse_lazy('catalog_app:index')
