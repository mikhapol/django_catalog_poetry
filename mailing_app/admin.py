from django.contrib import admin

from mailing_app.models import Buyer, MailingLog, MailingMessage, MailingSettings


# Register your models here.

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email')
    list_filter = ('last_name',)
    search_fields = ('last_name', 'email')



