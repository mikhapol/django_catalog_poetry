from django.db import models

NULLABLE = {'blank': True, 'null': True}
NOT_NULLABLE = {'blank': False, 'null': False}


class MailingMessage(models.Model):
    letter_subject = models.CharField(max_length=100, verbose_name='тема письма')
    letter_body = models.TextField(verbose_name='тело письма', **NULLABLE)

    def __str__(self):
        return f"Настройки письма - {self.letter_subject}"

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
