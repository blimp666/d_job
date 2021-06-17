# Generated by Django 3.2.4 on 2021-06-17 10:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210617_1019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='application',
            new_name='conference',
        ),
        migrations.AlterField(
            model_name='conference',
            name='date_start',
            field=models.DateField(default=datetime.datetime(2021, 6, 17, 10, 30, 0, 482699), verbose_name='Дата проведения'),
        ),
    ]