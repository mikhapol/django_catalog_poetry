from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from catalog_app.forms import ProviderForm
from catalog_app.models.provider import Provider


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
