from django import forms

from mailing_app.models import MailingSettings, Buyer, MailingMessage


class MailingSettingsForm(forms.ModelForm):
    class Meta:
        model = MailingSettings
        fields = ('status', 'period', 'time',)


class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ('first_name', 'last_name', 'email',)


class MessageForm(forms.ModelForm):
    class Meta:
        model = MailingMessage
        fields = ('letter_subject', 'letter_body',)
