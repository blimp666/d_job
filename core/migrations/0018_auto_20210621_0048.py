# Generated by Django 3.2.4 on 2021-06-21 00:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20210619_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='file',
            field=models.FileField(default='', upload_to='app_files', verbose_name='Работа'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2021, 6, 21, 0, 48, 43, 294739), verbose_name='Дата проведения'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='file',
            field=models.FileField(default='', upload_to='conf_files', verbose_name='Вложения'),
        ),
    ]