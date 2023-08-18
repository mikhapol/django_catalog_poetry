from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from mailing_app.forms import MailingSettingsForm, BuyerForm, MessageForm
from mailing_app.models import MailingSettings, Buyer, MailingClient


class MailingClientListView(ListView):
    model = MailingClient

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['buyer'] = Buyer.objects.all()
        context_data['mailing_pk'] = self.kwargs.get('pk')

        return context_data


def toggle_client(request, pk, client_pk):
    if MailingClient.objects.filter(
            buyer_id=client_pk,
            settings_id=pk
    ).exists():
        MailingClient.objects.filter(
            buyer_id=client_pk,
            settings_id=pk
        ).delete()
    else:
        MailingClient.objects.create(
            buyer_id=client_pk,
            settings_id=pk
        )
    return redirect(reverse('', args=[pk]))
