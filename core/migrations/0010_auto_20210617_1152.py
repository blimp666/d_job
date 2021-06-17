# Generated by Django 3.2.4 on 2021-06-17 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210617_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='conference',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2021, 6, 17, 11, 52, 5, 198794), verbose_name='Дата проведения'),
        ),
    ]
