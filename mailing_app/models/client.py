from django.db import models

from catalog_app.models.products import NULLABLE


class MailingClient(models.Model):
    buyer = models.ForeignKey('Buyer', on_delete=models.CASCADE, verbose_name='покупатель')
    settings = models.ForeignKey('MailingSettings', on_delete=models.CASCADE, verbose_name='настройки')

    def __str__(self):
        return f"{self.buyer} / {self.settings}"

    class Meta:
        verbose_name = 'Покупатель рассылки'
        verbose_name_plural = 'Покупатели рассылки'
