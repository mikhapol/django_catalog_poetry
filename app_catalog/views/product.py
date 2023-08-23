from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from app_catalog.forms import ProductForm, VersionForm
from app_catalog.models import Product, Version


class ProductListView(ListView):
    model = Product
    extra_context = {
        'title': 'Продукты'
    }


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'app_catalog.add_product'
    success_url = reverse_lazy('app_catalog:index')
    login_url = 'app_users:login'

    def form_valid(self, form):
        self.object = form.save()
        self.object.vendor = self.request.user
        self.object.save()

        return super().form_valid(form)

    extra_context = {
        'title': 'Добавление продукта'
    }


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'app_catalog.change_product'
    success_url = reverse_lazy('app_catalog:index')
    login_url = 'app_users:login'

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


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('app_catalog:index')
    login_url = 'app_users:login'

    def test_func(self):
        return self.request.user.is_superuser

    extra_context = {
        'title': f'Удаление'
    }
