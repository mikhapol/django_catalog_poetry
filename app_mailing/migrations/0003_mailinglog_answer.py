# Generated by Django 4.2.3 on 2023-08-22 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_mailing', '0002_alter_mailingsettings_end_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailinglog',
            name='answer',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ответ сервера'),
        ),
    ]
