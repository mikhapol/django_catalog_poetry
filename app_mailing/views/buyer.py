from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from app_mailing.forms import BuyerForm
from app_mailing.models import Buyer


class BuyerListView(ListView):
    model = Buyer


class BuyerCreateView(CreateView):
    model = Buyer
    form_class = BuyerForm
    success_url = reverse_lazy('app_mailing:buyers')


class BuyerUpdateView(UpdateView):
    model = Buyer
    form_class = BuyerForm
    success_url = reverse_lazy('app_mailing:buyers')


class BuyerDeleteView(DeleteView):
    model = Buyer
    success_url = reverse_lazy('app_mailing:buyers')
