from django.db import models

NULLABlE = {'blank': True, 'null': True}
NOT_NULLABLE = {'blank': False, 'null': False}


class MailingSettings(models.Model):
    pass

    def __str__(self):
        pass

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


