# Generated by Django 3.2.4 on 2021-06-14 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210611_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='name',
        ),
        migrations.AddField(
            model_name='application',
            name='description',
            field=models.CharField(default='', max_length=40, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='conference',
            name='file',
            field=models.FileField(blank=True, upload_to='media', verbose_name='Вложения'),
        ),
        migrations.AddField(
            model_name='conference',
            name='requirements',
            field=models.CharField(blank=True, default=' ', max_length=200, verbose_name='Требования'),
        ),
    ]
