from django.db import models

NULLABlE = {
    'blank': True,
    'null': True
}

NOT_NULLABLE = {
    'blank': False,
    'null': False
}


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя', **NOT_NULLABLE)
    desc = models.TextField(verbose_name='Описание', **NULLABlE)
    image = models.ImageField(upload_to='products/', verbose_name="Картинка", **NULLABlE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Категория")
    price = models.PositiveIntegerField(default=0, verbose_name="Цена", **NOT_NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", **NOT_NULLABLE)
    update_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления", **NOT_NULLABLE)

    def __str__(self):
        return f'Наименование - {self.name}, описание: {self.desc}, категория: {self.category}, цена - {self.price}.'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('price',)
