from django.db import models

from catalog_app.models.products import NULLABLE


class Buyer(models.Model):
    objects = None
    email = models.EmailField(verbose_name='Почта для рассылки', unique=True)
    first_name = models.CharField(max_length=100, verbose_name='имя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия')
    middle_name = models.CharField(max_length=100, verbose_name='отчество', **NULLABLE)
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
