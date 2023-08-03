# Generated by Django 4.2.3 on 2023-08-03 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='имя')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='почта')),
            ],
            options={
                'verbose_name': 'Владелец',
                'verbose_name_plural': 'Владельцы',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Продукт')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Картинка')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog_app.category', verbose_name='Категория')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog_app.owner', verbose_name='владелец')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ('price',),
            },
        ),
    ]
