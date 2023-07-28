from django.db import models


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


class Buyer(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя')
    email = models.EmailField(verbose_name='почта', unique=True)

    def __str__(self):
        return f'{self.email} ({self.name})'

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
