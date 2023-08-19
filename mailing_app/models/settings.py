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
        (STATUS_STARTED, 'started'),
        (STATUS_DONE, 'done'),
    )

    # time = models.TimeField(verbose_name='время')
    start_time = models.DateTimeField(verbose_name='Время старта', **NULLABLE)
    end_time = models.DateTimeField(verbose_name='Время окончания', **NULLABLE)
    period = models.CharField(max_length=20, choices=PERIODS, default=PERIOD_DAILY, verbose_name='Период')
    status = models.CharField(max_length=20, choices=STATUSES, default=STATUS_CREATED, verbose_name='Статус')

    message = models.ForeignKey('MailingMessage', on_delete=models.CASCADE, verbose_name='Сообщение', **NULLABLE)

    def __str__(self):
        return f"{self.start_time} / {self.period}"

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
