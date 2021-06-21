# coding: utf-8
import io
import os

from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.files import File
from django.db.models import F, Value
from django.db.models.functions import Concat
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from docxtpl import DocxTemplate

from core.enums import StatusEnum
from core.forms import CreateApplication, EditApplication, FilterField
from core.forms import CreateConference
from core.forms import LoginForm
from core.forms import UserProfileForm
from core.models import Application
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

    return render(
        request,
        'core/conference.html', {'conferences': conferences}
    )


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
                date_start=form.cleaned_data.get('date_start'),
                description=form.cleaned_data.get('description'),
            )
            conference_obj.file = request.FILES['file']
            conference_obj.save()
            return redirect('/')
    else:
        form = CreateConference()
    return render(request, 'core/create_conference.html', {'form': form})


def create_application(request, conference_id):
    """Рендер формы подачи заявки."""
    userprofile = UserProfile.objects.filter(
        user=request.user
    )
    if request.method == 'POST':
        form = CreateApplication(request.POST, request.FILES)
        if form.is_valid():
            if userprofile:
                application = Application.objects.filter(
                    participant=userprofile.get(),
                    conference=conference_id
                )
                if application:
                    application = application.get()
                    application.file = request.FILES['file']
                    application.description = form.cleaned_data['description']
                else:
                    application = Application.objects.create(
                        description=form.cleaned_data.get('description')
                    )
                    application.participant.add(userprofile.get())
                    application.conference.add(
                        Conference.objects.get(id=conference_id)
                    )
                    if request.FILES:
                        application.file = request.FILES['file']
                application.save()
            return redirect('/')
    else:
        form = CreateApplication()
    return render(request, 'core/create_application.html', {
        'form': form,
        'userprofile': userprofile
    })


def application_view(request):
    """Рендер страницы с поданными заявки для администратора."""
    userprofile = UserProfile.objects.filter(
        user=request.user
    )
    if userprofile:
        conferences = Conference.objects.filter(
            application__participant=userprofile.get()
        )
        applications = Application.objects.filter(
            participant=userprofile.get(),
            conference__in=conferences
        )
        conferences_list = []
        for conf in conferences:
            conf.app_description = applications.get(
                conference=conf.id
            ).description
            conf.app_file = applications.get(
                conference=conf.id
            ).file
            conf.status = applications.get(
                conference=conf.id
            ).status
            conf.app_id = applications.get(
                conference=conf.id
            ).id
            conferences_list.append(conf)
    return render(request, 'core/application_view.html', {
        'conferences': conferences_list,
        'userprofile': userprofile,
    })


def view_application_all(request):
    """Рендер страницы со всеми заявками."""
    applications = Application.objects.all()
    for application in applications:
        application.conf_name = applications.filter(
            id=application.id
        ).values_list(
            'conference__theme', flat=True
        ).get()
        application.author = UserProfile.objects.get(
            application=application.id
        ).fullname()
        application.author_degree = UserProfile.objects.get(
            application=application.id
        ).degree
    return render(request, 'core/application_all.html', {
        'applications': applications
    })


def edit_application(request, app_id):
    """Рендер формы редактирования заявки."""
    application = Application.objects.get(id=app_id)
    if request.method == 'POST':
        form = EditApplication(request.POST, request.FILES)
        if form.is_valid():
            application.description = form.cleaned_data.get('description')
            if request.FILES:
                application.file = request.FILES['file']
            application.status = StatusEnum.NEW.value
            application.save()
            return redirect('/')
    else:
        form = EditApplication(instance=application)
    return render(request, 'core/create_application.html', {'form': form})


def view_applications(request, conf_id):
    """Рендер страницы с поданными заявки для одной конференции."""
    applications = Application.objects.filter(
        conference=conf_id
    )
    for application in applications:
        application.author = applications.filter(
            id=application.id
        ).annotate(
            fullname=Concat(
                F('participant__surname'),
                Value(' '),
                F('participant__name'),
                Value(' '),
                F('participant__patronymic')
            )
        ).values_list('fullname', flat=True).get()
        application.degree = applications.filter(
            id=application.id
        ).values_list(
            'participant__degree', flat=True
        ).get()
    return render(request, 'core/check_apps.html', {
        'applications': applications
    })


def edit_conference(request, conf_id):
    """Рендер формы редактирования конференции."""
    conference_obj = Conference.objects.get(id=conf_id)
    if request.method == 'POST':
        form = CreateConference(request.POST, request.FILES)
        if form.is_valid():
            conference_obj.theme = form.cleaned_data.get('theme')
            conference_obj.date_start = form.cleaned_data.get('date_start')
            conference_obj.description = form.cleaned_data.get('description')
            conference_obj.file = request.FILES['file']
            conference_obj.save()
            return redirect('/')
    else:
        form = CreateConference(instance=conference_obj)
    return render(request, 'core/edit_conference.html', {'form': form})


def accept(request, app_id):
    """Принять зявку."""
    application = Application.objects.get(id=app_id)
    application.status = StatusEnum.ACCEPT.value
    application.save()
    return redirect('/view_all_applications')


def decline(request, app_id):
    """Отклонить зявку."""
    application = Application.objects.get(id=app_id)
    application.status = StatusEnum.DECLINE.value
    application.save()
    return redirect('/view_all_applications')


def conference_report(request, conf_id):
    """Печать отчёта по одной конференции."""
    doc = DocxTemplate('templates/core/reports/uchastnik.docx')
    applications = Application.objects.filter(
        conference__id=conf_id
    )
    context = {'participant': 'ХУЙ'}
    doc.render(context)
    doc.save('otchet-uchastnik.docx')
    doc_io = io.BytesIO()
    doc.save(doc_io)
    doc_io.seek(0)
    response = HttpResponse(doc_io.read())
    response['Content-Disposition'] = 'attachment; filename=otchet-uchastnik.docx'
    response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'

    return response
