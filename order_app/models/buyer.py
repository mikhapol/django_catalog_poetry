from django.db import models

NULLABlE = {'blank': True, 'null': True}
NOT_NULLABLE = {'blank': False, 'null': False}


class Buyer(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя')
    email = models.EmailField(verbose_name='почта', unique=True)

    def __str__(self):
        return f'{self.email} ({self.name})'

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
