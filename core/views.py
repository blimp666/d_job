# coding: utf-8
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from core.forms import CreateConference
from core.forms import LoginForm
from core.forms import UserProfileForm
from core.models import Conference
from core.models import UserProfile


def home_page(request):
    """Рендер главной страницы."""

    if getattr(request.user, 'id'):
        userprofile = UserProfile.objects.get(
            user_id=request.user.id
        )
        if request.user.is_superuser:
            is_admin = True
        else:
            is_admin = False
    else:
        userprofile = None
        is_admin = False
    return render(request, 'core/home_page.html', {
        'userprofile': userprofile,
        'is_admin': is_admin,
    })


def registration(request):
    """Рендер формы регистрации."""
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            surname = form.cleaned_data.get('surname')
            user = User.objects.get_or_create(
                username=username,
                password=raw_password,
                email=email,
                first_name=name,
                last_name=surname
            )
            if user:
                user[0].save()
                userprofile = UserProfile.objects.get_or_create(
                    user_id=user[0].id,
                    surname=surname,
                    name=name,
                    patronymic=form.cleaned_data.get('patronymic'),
                    email=form.cleaned_data.get('email'),
                    password=form.cleaned_data.get('password'),
                    office=form.cleaned_data.get('office'),
                    degree=form.cleaned_data.get('degree'),
                    organization=form.cleaned_data.get('organization'),
                    address=form.cleaned_data.get('address'),
                    phone=form.cleaned_data.get('phone'),
                    personal_data=form.cleaned_data.get('personal_data'),
                )
                userprofile[0].save()
                login(request, user[0])
            return redirect('/')
    else:
        form = UserProfileForm()
    return render(request, 'core/registration.html', {'form': form})


def conference(request):
    """Рендер страницы с конференциями."""

    conferences = Conference.objects.all()
    return render(request, 'core/conference.html', {'conferences': conferences})


def archive(request):
    """Рендер страницы с архивом."""

    return render(request, 'core/archive.html')


def news(request):
    """Рендер страницы новостей."""

    return render(request, 'core/news.html')


def log_out(request):
    """Выход из профиля."""

    auth.logout(request)
    return redirect('/')


def log_in(request):
    """Страница для авторизации."""

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            raw_password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = User.objects.filter(
                username=email,
                password=raw_password
            )
            if user:
                login(request, user.get())
                return redirect('/')
            else:
                return HttpResponse('Неверное имя или пароль.')
    else:
        form = LoginForm()
    return render(request, 'core/login.html', {'form': form})


def create_conference(request):
    """Рендер страницы для создания конференции."""

    if request.method == 'POST':
        form = CreateConference(request.POST, request.FILES)
        if form.is_valid():
            conference_obj = Conference.objects.create(
                theme=form.cleaned_data.get('theme'),
                count_participant=form.cleaned_data.get('count_participant'),
                date_start=form.cleaned_data.get('date_start'),
                description=form.cleaned_data.get('description')
            )
            conference_obj.save()
            return redirect('/')
    else:
        form = CreateConference()
    return render(request, 'core/create_conference.html', {'form': form})
