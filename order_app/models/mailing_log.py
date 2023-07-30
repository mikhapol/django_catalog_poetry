from django.db import models

NULLABlE = {'blank': True, 'null': True}
NOT_NULLABLE = {'blank': False, 'null': False}


class MailingLog(models.Model):
    data_log = models.DateTimeField(verbose_name='дата и время последней попытки')
    status_log = models.BooleanField(verbose_name='статус попытки')
    def __str__(self):
        pass

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
