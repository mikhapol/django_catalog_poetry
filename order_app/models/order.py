from django.db import models
from order_app.models import Buyer

NULLABlE = {'blank': True, 'null': True}
NOT_NULLABLE = {'blank': False, 'null': False}


class Order(models.Model):
    name = models.ForeignKey('catalog_app.Product', on_delete=models.CASCADE, verbose_name='продукт')

    name_buyer = models.ForeignKey('order_app.Buyer', on_delete=models.CASCADE, verbose_name='имя')
    message_buyer = models.TextField()

    closed = models.BooleanField(default=False, verbose_name='заказ закрыт')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.name_buyer} ({Buyer.email}) покупает {self.name}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
