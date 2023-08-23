from django import forms

from app_mailing.models import MailingSettings, Buyer, MailingMessage


class MailingSettingsForm(forms.ModelForm):
    class Meta:
        model = MailingSettings
        fields = ('start_time', 'end_time', 'status', 'period', 'message')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_time'].widget.attrs['placeholder'] = 'YYYY-MM-DD'
        self.fields['end_time'].widget.attrs['placeholder'] = 'YYYY-MM-DD'


class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ('first_name', 'last_name', 'email',)


class MessageForm(forms.ModelForm):
    class Meta:
        model = MailingMessage
        fields = ('letter_subject', 'letter_body',)
