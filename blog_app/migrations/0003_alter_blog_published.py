# Generated by Django 4.2.3 on 2023-07-23 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_alter_blog_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published',
            field=models.BooleanField(default=False, verbose_name='признак публикации'),
        ),
    ]
