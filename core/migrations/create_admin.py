# coding: utf-8
from __future__ import unicode_literals
from django.db import migrations


def create_superuser(apps, schema_editor):
    UserProfile = apps.get_model('core', 'UserProfile')
    User = apps.get_model('auth', 'User')
    user = User.objects.create(
        is_superuser=True,
        password='t476eeKl10z',
        username='iya.p0stnova@gmail.com',
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
        ('core', '0015_auto_20210617_1611'),
    ]

    operations = [
        migrations.RunPython(create_superuser, migrations.RunPython.noop)
    ]
