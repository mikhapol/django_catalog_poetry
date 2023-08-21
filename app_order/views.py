from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from app_catalog.models import Product
from app_order.forms import OrderForm
from app_order.models import Order
from app_order.services import send_order_email


class OrderCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    permission_required = 'app_order.add_order'

    def get_success_url(self):
        return reverse('app_catalog:view_product', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['product'] = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        return context_data

    def form_valid(self, form):
        obj = form.save()
        send_order_email(obj)
        return super().form_valid(form)
