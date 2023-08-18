from django.db import models

from catalog_app.models.products import NULLABLE


class MailingSettings(models.Model):
    PERIOD_DAILY = 'daily'
    PERIOD_WEEKLY = 'weekly'
    PERIOD_MONTHLY = 'monthly'
    PERIODS = (
        (PERIOD_DAILY, 'Ежедневная'),
        (PERIOD_WEEKLY, 'Раз в неделю'),
        (PERIOD_MONTHLY, 'Раз в месяц'),
    )

    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_DONE = 'done'
    STATUSES = (
        (STATUS_CREATED, 'created'),
        (STATUS_STARTED,'started'),
        (STATUS_DONE, 'done'),
    )

    time = models.TimeField(verbose_name='время')
    period = models.CharField(max_length=20, choices=PERIODS, default=PERIOD_DAILY, verbose_name='Период')
    status = models.CharField(max_length=20, choices=STATUSES, default=STATUS_CREATED, verbose_name='Статус')

    message = models.ForeignKey('MailingMessage', on_delete=models.CASCADE, verbose_name='Сообщение', **NULLABLE)

    def __str__(self):
        return (f"{self.time} / {self.period}")

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'



    # mailing_time = models.TimeField(verbose_name='время рассылки')
    #
    # frequency = models.CharField(max_length=100, choices=[
    #     ('daily', 'Раз в день'),
    #     ('weekly', 'Раз в неделю'),
    #     ('monthly', 'Раз в месяц')
    # ])
    # mailing_status = models.CharField(max_length=100, choices=[
    #     ('established', 'создана'),
    #     ('launched', 'запущена'),
    #     ('completed', 'завершена'),
    # ])
    #
    # buyer = models.ForeignKey('Buyer', on_delete=models.CASCADE, verbose_name='покупатель')
    # message = models.ForeignKey('MailingMessage', on_delete=models.CASCADE, verbose_name='сообщение')
    #

