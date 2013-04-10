# -*- coding=utf8 -*-
from django.conf.urls.defaults import patterns, url
from views import DokladEdit, DokladList, ShowSection

#Урлы для настройки профиля пользователя
urlpatterns = patterns('',
    url(r'^profile/dokladedit/$', DokladEdit),
    url(r'^profile/dokladlist/$', DokladList),
    url(r'^section/$', ShowSection),
    )
