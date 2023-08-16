from django.db import models

from catalog_app.models import Product


class Provider(models.Model):
    title = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'поставщик'
        verbose_name_plural = 'поставщики'
