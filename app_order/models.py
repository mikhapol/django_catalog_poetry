from django.db import models


# Create your models here.
class Order(models.Model):
    product = models.ForeignKey('app_catalog.Product', on_delete=models.CASCADE, verbose_name='продукт')

    name = models.CharField(max_length=150, verbose_name='имя')
    email = models.EmailField(max_length=150, verbose_name='почта')
    message = models.TextField()

    closed = models.BooleanField(default=False, verbose_name='заказ закрыт')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.product} от {self.email}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
