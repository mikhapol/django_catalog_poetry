__all__ = [
    'BuyerListView',
    'BuyerCreateView',
    'BuyerUpdateView',
    'BuyerDeleteView',
    'MailingClientListView',
    'MessageListView',
    'MessageCreateView',
    'MessageUpdateView',
    'MessageDeleteView',
    'MailingListView',
    'MailingSettingsCreateView',
    'MailingSettingsUpdateView',
    'MailingSettingsDeleteView',
    'toggle_client',
]

from mailing_app.views.buyer import BuyerListView, BuyerUpdateView, BuyerDeleteView, BuyerCreateView
from mailing_app.views.client import MailingClientListView, toggle_client
from mailing_app.views.message import MessageListView, MessageUpdateView, MessageDeleteView, MessageCreateView
from mailing_app.views.settings import MailingListView, MailingSettingsUpdateView, MailingSettingsDeleteView, \
    MailingSettingsCreateView
