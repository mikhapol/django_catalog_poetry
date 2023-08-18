from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from mailing_app.forms import BuyerForm
from mailing_app.models import Buyer


class BuyerListView(ListView):
    model = Buyer


class BuyerCreateView(CreateView):
    model = Buyer
    form_class = BuyerForm
    success_url = reverse_lazy('mailing_app:buyers')


class BuyerUpdateView(UpdateView):
    model = Buyer
    form_class = BuyerForm
    success_url = reverse_lazy('mailing_app:buyers')


class BuyerDeleteView(DeleteView):
    model = Buyer
    success_url = reverse_lazy('mailing_app:buyers')
