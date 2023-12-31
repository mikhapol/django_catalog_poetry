from django.contrib import admin

from app_mailing.models import Buyer, MailingMessage, MailingSettings, MailingLog, MailingClient


# Register your models here.

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email')
    list_filter = ('last_name',)
    search_fields = ('last_name', 'email')


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = ('letter_subject', 'letter_body')
    list_filter = ('letter_subject',)
    search_fields = ('letter_subject',)


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'period', 'status', 'message')


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('last_attempt', 'status', 'buyer', 'settings')
    list_filter = ('last_attempt',)


@admin.register(MailingClient)
class MailingClientAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'settings')
