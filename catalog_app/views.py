from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView

from catalog_app.forms import ProviderForm, ProductForm, VersionForm
from catalog_app.models import Product, Category, Version
from catalog_app.models.provider import Provider


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

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        contex_data['category_id'] = category_item.pk,
        contex_data['title'] = f'Все продукты категории {category_item.name}'

        return contex_data


class ContactTemplateView(TemplateView):
    template_name = 'catalog_app/contacts.html'
    extra_context = {
        'title': 'Контакты'
    }

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        if self.request.method == 'POST':
            name = self.request.POST.get('name')
            phone = self.request.POST.get('phone')
            message = self.request.POST.get('message')
            print(f'Новое сообщение от {name} ({phone}): {message}')
        return super().get_context_data(**kwargs)


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog_app:index')

    extra_context = {
        'title': 'Добавление продукта'
    }


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog_app:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormSet(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormSet(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    extra_context = {
        'title': 'Редактирование продукта'
    }


class ProductDetailView(DetailView):
    model = Product
    extra_context = {
        'title': 'Информация о продукте.'
    }


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog_app:index')
    extra_context = {
        'title': f'Удаление'
    }


class ProviderCreateView(CreateView):
    model = Provider
    form_class = ProviderForm
    success_url = reverse_lazy('catalog_app:index')
    extra_context = {
        'title': 'Добавление поставщика'
    }


class ProviderUpdateView(UpdateView):
    model = Provider
    fields = '__all__'
    success_url = reverse_lazy('catalog_app:index')

    extra_context = {
        'title': 'Изменение'
    }
