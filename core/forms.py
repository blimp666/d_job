# coding: utf-8
from django import forms
from django.forms import ModelForm
from django.forms import PasswordInput
from core.models import Application
from core.models import Conference
from core.models import UserProfile


class UserProfileForm(ModelForm):
    """Форма для создания профиля пользователя."""

    class Meta:
        model = UserProfile
        fields = [
            'surname',
            'name',
            'patronymic',
            'email',
            'password',
            'office',
            'degree',
            'organization',
            'address',
            'phone',
            'personal_data'
        ]
        widgets = {
            'password': PasswordInput(),
        }


class LoginForm(UserProfileForm):
    """Форма для авторизации."""

    class Meta:
        model = UserProfile
        fields = [
            'email',
            'password',
        ]
        widgets = {
            'password': PasswordInput(),
        }


class CreateConference(ModelForm):
    """Форма для создания конференции."""

    class Meta:
        model = Conference
        fields = [
            'theme',
            'date_start',
            'description',
            'requirements',
            'file'
        ]


class CreateApplication(ModelForm):
    """Форма для создания заявки"""

    class Meta:
        model = Application
        fields = [
            'description',
            'file'
        ]


class EditApplication(ModelForm):
    """Форма для редактирования заявки"""

    class Meta:
        model = Application
        fields = [
            'description',
            'file'
        ]


class FilterField(forms.Form):
    selected = forms.ChoiceField(

    )

    class Meta:
        fields = ['selected']
