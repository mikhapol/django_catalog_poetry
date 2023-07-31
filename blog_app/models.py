from django.db import models

NULLABLE = {'blank': True, 'null': True}
NOT_NULLABLE = {'blank': False, 'null': False}


class Blog(models.Model):
    name_blog = models.CharField(max_length=50, verbose_name='заголовок', **NOT_NULLABLE)
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    body = models.TextField(verbose_name='содержимое', **NOT_NULLABLE)
    image = models.ImageField(upload_to='blog/', verbose_name="превью", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата создания", **NOT_NULLABLE)
    published = models.BooleanField(default=False, verbose_name='признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return self.name_blog

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
