from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from catalog_app.forms import ProductForm, VersionForm
from catalog_app.models import Product, Version


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Продукты'
    }


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
        VersionFormSet = inlineformset_factory(self.model, Version, form=VersionForm, extra=1)
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
