import datetime

from django.conf import settings
from django.core.mail import send_mail

from mailing_app.models import MailingSettings, MailingLog


def send_email(message_settings, message_buyer):
    result = send_mail(
        subject=message_settings.message.letter_subject,
        message=message_settings.message.letter_body,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[message_buyer.buyer.email],
        fail_silently=False,
    )

    MailingLog.objects.create(
        status=MailingLog.STATUS_OK if result else MailingLog.STATUS_FAILED,
        settings=message_settings,
        buyer_id=message_buyer.buyer_id
    )


# def send_mails():
#     for m_s in MailingSettings.objects.filter(status=MailingSettings.STATUS_STARTED):
#         for m_c in m_s.mailingclient_set.all():
#             send_email(m_s, m_c)

def send_mails():
    datetime_now = datetime.datetime.now(datetime.timezone.utc)
    for mailing_setting in MailingSettings.objects.filter(status=MailingSettings.STATUS_STARTED):

        if (datetime_now > mailing_setting.start_time) and (datetime_now < mailing_setting.end_time):

            for mailing_client in mailing_setting.mailingclient_set.all():

                mailing_log = MailingLog.objects.filter(
                    buyer=mailing_client.buyer,
                    settings=mailing_setting
                )

                if mailing_log.exists():
                    last_try_date = mailing_log.order_by('-last_attempt').first().last_attempt

                    if mailing_log.period == MailingSettings.PERIOD_DAILY:
                        if (datetime_now - last_try_date).days >= 1:
                            send_email(mailing_setting, mailing_client)
                    elif mailing_setting.period == MailingSettings.PERIOD_WEEKLY:
                        if (datetime_now - last_try_date).days >= 7:
                            send_email(mailing_setting, mailing_client)
                    elif mailing_setting.period == MailingSettings.PERIOD_MONTHLY:
                        if (datetime_now - last_try_date).days >= 30:
                            send_email(mailing_setting, mailing_client)

                else:
                    send_email(mailing_setting, mailing_client)
