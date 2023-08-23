from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from app_mailing.forms import BuyerForm
from app_mailing.models import Buyer


class BuyerListView(LoginRequiredMixin, ListView):
    model = Buyer

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('app_mailing.view_buyer'):
            return queryset
        return queryset.filter(owner=self.request.user)


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
