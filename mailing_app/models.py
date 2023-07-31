from django.db import models

NULLABLE = {'blank': True, 'null': True}
NOT_NULLABLE = {'blank': False, 'null': False}


class Buyer(models.Model):
    email = models.EmailField(verbose_name='Email', unique=True)
    fullname = models.CharField(max_length=100, verbose_name='ФИО')
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return f"{self.fullname} ({self.email})"

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


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


class MailingMessage(models.Model):
    letter_subject = models.CharField(max_length=100, verbose_name='тема письма')
    letter_body = models.TextField(verbose_name='тело письма', **NULLABLE)

    def __str__(self):
        return f"Настройки письма - {self.letter_subject}"

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


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
