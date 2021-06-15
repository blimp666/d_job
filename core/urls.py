# coding: utf-8
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from conference1 import settings
from core.views import archive
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
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
