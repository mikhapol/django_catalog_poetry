from django.db import models


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')
    version_number = models.PositiveIntegerField(default=0, verbose_name="номер версии")
    version_name = models.CharField(max_length=20, verbose_name='Описание')
    is_actual = models.BooleanField(default=True, verbose_name='Признак текущей версии')

    def __str__(self):
        return f'{self.product} - {self.version_name} ({self.is_actual}).'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
