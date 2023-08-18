from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from catalog_app.forms import ProviderForm
from catalog_app.models.provider import Provider


class ProviderCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Provider
    form_class = ProviderForm
    permission_required = 'catalog_app.add_provider'
    success_url = reverse_lazy('catalog_app:index')
    extra_context = {
        'title': 'Добавление поставщика'
    }


class ProviderUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Provider
    fields = '__all__'
    permission_required = 'catalog_app.change_provider'
    success_url = reverse_lazy('catalog_app:index')

    extra_context = {
        'title': 'Изменение'
    }
