from django import forms

from app_catalog.forms import StyleFormMixin
from app_order.models import Order


class OrderForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
