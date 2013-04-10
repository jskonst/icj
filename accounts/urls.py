# -*- coding=utf8 -*-
from django.conf.urls.defaults import patterns, url
from forms import UserRegistrationForm
from views import profile, userlist, userbage

#Урлы для настройки профиля пользователя
urlpatterns = patterns('',
    url(r'^userlist/$', userlist),
    url(r'^userbage/$', userbage),
    url(r'^profile/$', profile),
    url(r'^register/$', 'registration.views.register', {'backend': 'accounts.backend.RegBackend', 'form_class': UserRegistrationForm}, name='registration_register'),
    )
