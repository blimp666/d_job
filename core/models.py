# coding: utf-8
import datetime
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from core.enums import StatusEnum


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
    # image = models.ImageField(
    #     verbose_name='Изображение',
    #     blank=True,
    #     null=True,
    #     upload_to='user_images',
    # )

    def fullname(self):
        return '{} {} {}'.format(self.surname, self.name, self.patronymic)

    def __str__(self):
        return self.fullname()

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


class Conference(models.Model):
    """Класс конференция."""

    theme = models.CharField(
        verbose_name='Название конференции',
        max_length=40,
    )
    date_start = models.DateField(
        verbose_name='Дата проведения',
        default=datetime.datetime.today(),
    )
    description = models.CharField(
        verbose_name='Описание',
        max_length=200,
        blank=True,
        default='',
    )
    requirements = models.CharField(
        verbose_name='Требования',
        max_length=200,
        blank=True,
        default='',
    )
    file = models.FileField(
        verbose_name='Вложения',
        upload_to='conf_files',
        default=''
    )

    def date_to_str(self):
        date_str = self.date_start.__format__('%d.%m.%y')
        return date_str

    class Meta:
        verbose_name = 'Конференция'
        verbose_name_plural = 'Конференции'


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
        upload_to='app_files',
        default=''
    )
    status = models.CharField(
        verbose_name='Статус заявки',
        max_length=20,
        default=StatusEnum.NEW.value,
    )
    conference = models.ManyToManyField(
        Conference,
    )

    class Meta:
        verbose_name = 'Заявка на участие'
        verbose_name_plural = 'Заявки на участие'
