from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from catalog_app.models import Product
from order_app.forms import OrderForm
from order_app.models import Order
from order_app.services import send_order_email


class OrderCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    permission_required = 'order_app.add_order'

    def get_success_url(self):
        return reverse('catalog_app:view_product', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['product'] = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        return context_data

    def form_valid(self, form):
        obj = form.save()
        send_order_email(obj)
        return super().form_valid(form)
