# coding: utf-8
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from conference1 import settings
from core.views import archive, edit_application, view_applications, \
    edit_conference, view_application_all, accept, decline, conference_report
from core.views import application_view
from core.views import create_application
from core.views import conference
from core.views import create_conference
from core.views import home_page
from core.views import log_in
from core.views import log_out
from core.views import news
from core.views import registration


urlpatterns = [
    path('', home_page),
    path('registration/', registration, name='registration'),
    path('conference/', conference, name='conference'),
    path('archive/', archive, name='archive'),
    path('news/', news, name='news'),
    path('logout/', log_out, name='logout'),
    path('login/', log_in, name='login'),
    path('create_conference/', create_conference, name='create_conference'),
    path(
        'create_application/<int:conference_id>',
        create_application,
        name='create_application'
    ),
    path(
        'edit_application/<int:app_id>',
        edit_application,
        name='edit_application'
    ),
    path(
        'view_applications/<int:conf_id>',
        view_applications,
        name='view_applications'
    ),
    path('application_view/', application_view, name='application_view'),
    path(
        'edit_conference/<int:conf_id>',
        edit_conference,
        name='edit_conference'
    ),
    path(
        'view_all_applications/',
        view_application_all,
        name='view_all_applications'
    ),
    path('accept/<int:app_id>', accept, name='accept'),
    path('decline/<int:app_id>', decline, name='decline'),
    path(
        'conference_report/<int:conf_id>',
        conference_report,
        name='conference_report'
    )
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
