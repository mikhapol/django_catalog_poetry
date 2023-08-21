from django.urls import path

from app_mailing.apps import AppMailingConfig

from app_mailing.views import (
    BuyerListView, BuyerCreateView, BuyerUpdateView, BuyerDeleteView, MailingClientListView, MessageListView,
    MessageCreateView, MessageUpdateView, MessageDeleteView, MailingListView, MailingSettingsCreateView,
    MailingSettingsUpdateView, MailingSettingsDeleteView, toggle_client
)

app_name = AppMailingConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing_list'),
    path('create/', MailingSettingsCreateView.as_view(), name='mailing_create'),
    path('update/<int:pk>/', MailingSettingsUpdateView.as_view(), name='mailing_update'),
    path('delete/<int:pk>/', MailingSettingsDeleteView.as_view(), name='mailing_delete'),

    path('<int:pk>/buyers/', MailingClientListView.as_view(), name='mailing_buyer'),
    path('<int:pk>/buyers/add/<int:buyer_pk>/', toggle_client, name='mailing_buyer_toggle'),

    path('buyers/', BuyerListView.as_view(), name='buyers'),
    path('buyers/create/', BuyerCreateView.as_view(), name='buyers_create'),
    path('buyers/update/<int:pk>/', BuyerUpdateView.as_view(), name='buyers_update'),
    path('buyers/delete/<int:pk>/', BuyerDeleteView.as_view(), name='buyers_delete'),

    path('messages/', MessageListView.as_view(), name='messages'),
    path('messages/create/', MessageCreateView.as_view(), name='messages_create'),
    path('messages/update/<int:pk>/', MessageUpdateView.as_view(), name='messages_update'),
    path('messages/delete/<int:pk>/', MessageDeleteView.as_view(), name='messages_delete'),
]
