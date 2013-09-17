# -*- coding=utf8 -*-
#from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import patterns, include, url
import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

    #url(r'^test/', 'testForms.views.contact'),
    url(r'^accounts/', include('accounts.urls')),
    # Подключаем урлы приложения конференция
    url(r'^accounts/', include('conference.urls')),
    url(r'^', include('conference.urls')),
    url(r'^', include('accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.urls')),
    url(r'^$', 'ICJ.views.home'),  # Основная страница с информацией
    url(r'^news/$', 'ICJ.views.news'),  # Новости
    url(r'^contact/$', 'ICJ.views.contacts'),  # Контакты
    url(r'^schedule/$', 'ICJ.views.schedule'),
    url(r'^agreement/$', 'ICJ.views.agreement'),
    #чтобы правильно отображать статику на сервере
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += staticfiles_urlpatterns()
