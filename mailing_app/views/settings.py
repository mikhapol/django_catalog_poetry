from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from mailing_app.forms import MailingSettingsForm
from mailing_app.models import MailingSettings


class MailingListView(ListView):
    model = MailingSettings


class MailingSettingsCreateView(CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing_app:mailing_list')


class MailingSettingsUpdateView(UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing_app:mailing_list')


class MailingSettingsDeleteView(DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailing_app:mailing_list')