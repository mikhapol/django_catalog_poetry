from django.db import models

from catalog_app.models.products import NULLABLE


class MailingLog(models.Model):
    STATUS_OK = 'ok'
    STATUS_FAILED = 'failed'
    STATUSES = (
        (STATUS_OK, 'Успешно'),
        (STATUS_FAILED, 'Ошибка'),
    )

    last_attempt = models.DateTimeField(auto_now_add=True, verbose_name='дата последней попытки')
    buyer = models.ForeignKey('Buyer', on_delete=models.CASCADE, verbose_name='покупатель')
    settings = models.ForeignKey('MailingSettings', on_delete=models.CASCADE, verbose_name='настройки')
    status = models.CharField(choices=STATUSES, default=STATUS_OK, verbose_name='статус')

    def __str__(self):
        return f"{self.last_attempt}"

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
