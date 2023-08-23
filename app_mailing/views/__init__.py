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
    'SendsAndBlogsView',
]

from app_mailing.views.buyer import BuyerListView, BuyerUpdateView, BuyerDeleteView, BuyerCreateView
from app_mailing.views.client import MailingClientListView, toggle_client
from app_mailing.views.message import MessageListView, MessageUpdateView, MessageDeleteView, MessageCreateView
from app_mailing.views.sends_and_blogs import SendsAndBlogsView
from app_mailing.views.settings import MailingListView, MailingSettingsUpdateView, MailingSettingsDeleteView, \
    MailingSettingsCreateView
