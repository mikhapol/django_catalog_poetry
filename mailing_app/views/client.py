from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView

from mailing_app.models import Buyer, MailingClient


class MailingClientListView(ListView):
    model = MailingClient

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['buyers'] = Buyer.objects.all()
        context_data['mailing_pk'] = self.kwargs.get('pk')

        return context_data

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(settings=self.kwargs.get('pk'))
        return queryset


def toggle_client(request, pk, buyer_pk):
    if MailingClient.objects.filter(
            buyer_id=buyer_pk,
            settings_id=pk
    ).exists():
        MailingClient.objects.filter(
            buyer_id=buyer_pk,
            settings_id=pk
        ).delete()
    else:
        MailingClient.objects.create(
            buyer_id=buyer_pk,
            settings_id=pk
        )
    return redirect(reverse('mailing_app:mailing_buyer', args=[pk]))
