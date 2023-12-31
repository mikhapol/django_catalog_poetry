from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from app_mailing.forms import MailingSettingsForm
from app_mailing.models import MailingSettings


class MailingListView(ListView):
    model = MailingSettings

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.has_perm('app_mailing.view_mailingsettings'):
            return queryset
        return queryset.filter(owner=self.request.user)


class MailingSettingsCreateView(CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('app_mailing:mailing_list')


class MailingSettingsUpdateView(UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('app_mailing:mailing_list')


class MailingSettingsDeleteView(DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('app_mailing:mailing_list')
