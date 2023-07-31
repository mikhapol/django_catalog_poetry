from django.contrib import admin

from mailing_app.models import Buyer, MailingLog, MailingMessage, MailingSettings


# Register your models here.

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'email')
    list_filter = ('fullname', 'email')
    search_fields = ('fullname', 'email')


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'attempt_status', 'last_attempt')
    list_filter = ('last_attempt', 'attempt_status')
    # search_fields = ()


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = ('letter_subject', 'letter_body')
    list_filter = ('letter_subject', 'letter_body')
    # search_fields = ()


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'message', 'mailing_time', 'frequency', 'mailing_status')
    list_filter = ('mailing_status', 'mailing_time')
    # search_fields = ()
