# coding: utf-8
"""Регистрация моделей в админке."""
from django.contrib import admin
from core.models import Application
from core.models import Conference
from core.models import UserProfile


admin.site.register(UserProfile)
admin.site.register(Application)
admin.site.register(Conference)
