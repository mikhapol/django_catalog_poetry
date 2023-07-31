from django.db import models


NULLABLE = {'blank': True, 'null': True}
NOT_NULLABLE = {'blank': False, 'null': False}


class MailingSettings(models.Model):
    mailing_time = models.TimeField(verbose_name='время рассылки')

    frequency = models.CharField(max_length=100, choices=[
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц')
    ])
    mailing_status = models.CharField(max_length=100, choices=[
        ('established', 'создана'),
        ('launched', 'запущена'),
        ('completed', 'завершена'),
    ])

    buyer = models.ForeignKey('Buyer', on_delete=models.CASCADE, verbose_name='покупатель')
    message = models.ForeignKey('MailingMessage', on_delete=models.CASCADE, verbose_name='сообщение')

    def __str__(self):
        return (f"Настройки рассылки - {self.frequency} ({self.mailing_time}{self.mailing_status})"
                f"Ваше сообщение: \n{self.message}")

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
