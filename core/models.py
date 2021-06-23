# coding: utf-8
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class UserProfile(models.Model):
    """Класс профиль пользователя."""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    name = models.CharField(max_length=30, verbose_name='Имя')
    patronymic = models.CharField(
        max_length=30,
        verbose_name='Отчество',
        blank=True
    )
    email = models.EmailField(verbose_name='Эл. почта')
    password = models.CharField(max_length=20, verbose_name='Пароль')
    office = models.CharField(
        max_length=30,
        verbose_name='Должность',
        blank=True,
        null=True,
    )
    degree = models.CharField(
        max_length=20,
        verbose_name='Степень',
        blank=True,
        null=True,
    )
    organization = models.CharField(
        max_length=30,
        verbose_name='Организация',
        blank=True,
        null=True,
    )
    address = models.CharField(
        max_length=60,
        verbose_name='Адрес',
        blank=True,
        null=True,
    )
    phone = models.IntegerField(
        verbose_name='Телефон',
        blank=True,
        null=True,
    )
    personal_data = models.BooleanField(
        verbose_name='Согласие на обработку персональных данных',
        default=False,
    )

    def fullname(self):
        return '{} {} {}'.join(self.surname, self.name, self.patronymic)

    def __str__(self):
        return self.fullname()

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


class Application(models.Model):
    """Класс заявка"""

    participant = models.ManyToManyField(
        UserProfile,
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=40,
        default='',
    )
    file = models.FileField(
        verbose_name='Работа',
        upload_to='media',
    )
    status = models.CharField(
        verbose_name='Статус заявки',
        blank=True,
        null=True,
        max_length=40,
    )

    class Meta:
        verbose_name = 'Заявка на участие'
        verbose_name_plural = 'Заявки на участие'


class Conference(models.Model):
    """Класс конференция."""

    theme = models.CharField(
        verbose_name='Название конференции',
        max_length=40,
    )
    application = models.ManyToManyField(
        Application,
    )
    count_participant = models.SmallIntegerField(
        verbose_name='Количество участников',
    )
    date_start = models.DateField(
        verbose_name='Дата проведения',
        default=timezone.now,
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=200,
        blank=True,
        default=' ',
    )
    requirements = models.CharField(
        verbose_name='Требования',
        max_length=200,
        blank=True,
        default=' ',
    )
    file = models.FileField(
        verbose_name='Вложения',
        upload_to='media',
        blank=True,
    )

    class Meta:
        verbose_name = 'Конференция'
        verbose_name_plural = 'Конференции'
