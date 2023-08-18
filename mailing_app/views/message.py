from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from mailing_app.forms import MailingSettingsForm, BuyerForm, MessageForm
from mailing_app.models import MailingSettings, Buyer, MailingClient, MailingMessage


class MessageListView(ListView):
    model = MailingMessage


class MessageCreateView(CreateView):
    model = MailingMessage
    form_class = MessageForm
    success_url = reverse_lazy('mailing_app:messages')


class MessageUpdateView(UpdateView):
    model = MailingMessage
    form_class = MessageForm
    success_url = reverse_lazy('mailing_app:messages')


class MessageDeleteView(DeleteView):
    model = MailingMessage
    success_url = reverse_lazy('mailing_app:messages')
