from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from app_catalog.forms import ProviderForm
from app_catalog.models.provider import Provider


class ProviderCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Provider
    form_class = ProviderForm
    permission_required = 'app_catalog.add_provider'
    success_url = reverse_lazy('app_catalog:index')
    extra_context = {
        'title': 'Добавление поставщика'
    }


class ProviderUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Provider
    fields = '__all__'
    permission_required = 'app_catalog.change_provider'
    success_url = reverse_lazy('app_catalog:index')

    extra_context = {
        'title': 'Изменение'
    }
