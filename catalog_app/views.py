from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from catalog_app.models import Product, Category


# Create your views here.


# def home(request):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list,
#         'title': 'Продукты'
#     }
#     return render(request, 'catalog_app/product_list.html', context)


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Продукты'
    }


class CategoryListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категория продуктов'
    }


class VegetablesListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        contex_data = super().get_context_data(*args, **kwargs)

        category_item = Product.objects.get(pk=self.kwargs.get('pk'))
        contex_data['category_id'] = category_item.pk
        contex_data['name'] = f'Продукты категории - все наши категории {category_item.name}'

        return contex_data


def vegetables(request, pk):
    category_items = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Продукты {category_items.name}.'
    }

    return render(request, 'catalog_app/vegetables_list.html', context)


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


def admin():
    pass


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'desc', 'price', 'category', 'image')
    success_url = reverse_lazy('catalog_app:index')

    extra_context = {
        'title': 'Добавление продукта'
    }


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'desc', 'price', 'category', 'image')
    success_url = reverse_lazy('catalog_app:index')

    extra_context = {
        'title': 'Изменение'
    }


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': f'Информация о продукте.'
    }


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog_app:index')
    extra_context = {
        'title': f'Удаление'
    }