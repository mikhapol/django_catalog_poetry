from django.conf import settings
from django.core.mail import send_mail

from mailing_app.models import MailingSettings, MailingLog


def send_email(message_settings, message_buyer):
    result = send_mail(
        subject=message_settings.message.subject,
        message=message_settings.message.message,
        from_email=settings.EMAIL_HOST_USER,
        # recipient_list=[message_buyer.buyer.email],
        recipient_list=['mikhapol@gmail.com', 'mikhapol@icloud.com'],
        fail_silently=False,
    )

    MailingLog.objects.create(
        status=MailingLog.STATUS_OK if result else MailingLog.STATUS_FAILED,
        settings=message_settings,
        # buyer=message_buyer,
        buyer_id=message_buyer.buyer_id
    )


def send_mails():
    for m_s in MailingSettings.objects.filter(status=MailingSettings.STATUS_STARTED):
        for m_c in m_s.mailingclient_set.all():
            send_mail(m_s, m_c)
