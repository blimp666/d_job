# coding: utf-8
"""Миграция для создания суперюзера."""
from __future__ import unicode_literals
from django.db import migrations


def create_superuser(apps, schema_editor):
    UserProfile = apps.get_model('core', 'UserProfile')
    User = apps.get_model('auth', 'User')
    user = User.objects.create(
        is_superuser=True,
        password='t476eeKl10z',
        username='admin_admin@gmail.com',
        email='iya.p0stnova@gmail.com',
        first_name='Администратор',
        last_name='',
        is_active=True
    )
    user.save()
    userprofile = UserProfile.objects.create(
        user_id=user.id,
        surname='Администраторов',
        name='Администратор',
        email='iya.p0stnova@gmail.com',
        password='t476eeKl10z'
    )
    userprofile.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20210618_2042'),
    ]

    operations = [
        migrations.RunPython(create_superuser, migrations.RunPython.noop)
    ]
