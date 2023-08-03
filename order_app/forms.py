from django import forms

from catalog_app.forms import StyleFormMixin
from order_app.models import Order


class OrderForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
