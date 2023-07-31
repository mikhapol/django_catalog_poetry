from django.db import models


NULLABLE = {'blank': True, 'null': True}
NOT_NULLABLE = {'blank': False, 'null': False}


class MailingLog(models.Model):
    last_attempt = models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки')
    attempt_status = models.BooleanField(default=True)
    mail_server = models.CharField(max_length=100, verbose_name='сервер', **NULLABLE)
    mailing = models.ForeignKey('MailingSettings', on_delete=models.CASCADE, verbose_name='рассылка')

    def __str__(self):
        return f"Cообщение от {self.last_attempt}"

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
