# Generated by Django 3.2.4 on 2021-06-17 15:58

import datetime
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20210617_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2021, 6, 17, 15, 58, 26, 96326), verbose_name='Дата проведения'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='file',
            field=models.FileField(upload_to=django.core.files.storage.FileSystemStorage(location='/media'), verbose_name='Вложения'),
        ),
    ]
