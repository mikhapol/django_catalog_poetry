from django.db import models

from app_catalog.models.products import NOT_NULLABLE, NULLABLE


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование', **NOT_NULLABLE)
    desc = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)
