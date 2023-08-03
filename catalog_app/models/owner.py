from django.db import models

NULLABLE = {'blank': True, 'null': True}

NOT_NULLABLE = {'blank': False, 'null': False}


class Owner(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя')
    email = models.EmailField(verbose_name='почта', unique=True)

    def __str__(self):
        return f'{self.email} ({self.name})'

    class Meta:
        verbose_name = 'Владелец'
        verbose_name_plural = 'Владельцы'

