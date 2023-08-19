from django.db import models

from catalog_app.models.products import NULLABLE


class MailingMessage(models.Model):
    letter_subject = models.CharField(max_length=100, verbose_name='тема письма')
    letter_body = models.TextField(verbose_name='тело письма', **NULLABLE)

    def __str__(self):
        return f"{self.letter_subject}"

    class Meta:
        verbose_name = 'Письма'
        verbose_name_plural = 'Письмо'
