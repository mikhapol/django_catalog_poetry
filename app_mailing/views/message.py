from django.urls import reverse_lazy
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)

from app_mailing.forms import MessageForm
from app_mailing.models import MailingMessage


class MessageListView(ListView):
    model = MailingMessage


class MessageCreateView(CreateView):
    model = MailingMessage
    form_class = MessageForm
    success_url = reverse_lazy('app_mailing:messages')


class MessageUpdateView(UpdateView):
    model = MailingMessage
    form_class = MessageForm
    success_url = reverse_lazy('app_mailing:messages')


class MessageDeleteView(DeleteView):
    model = MailingMessage
    success_url = reverse_lazy('app_mailing:messages')
