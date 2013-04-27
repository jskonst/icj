#-*- coding=utf8 -*-
'''
Created on 16.06.2012

@author: jskonst
'''
import glob
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import settings


def home(request):
	staticfile = settings.STATIC_ROOT + "info.html"
	info = open(staticfile)
	text = info.read()
	info.close()
	return render_to_response('test.html', {'content': text}, RequestContext(request))


def agreement(request):
	staticfile = settings.STATIC_ROOT + "agreement.html"
	info = open(staticfile)
	text = info.read()
	info.close()
	return render_to_response('agreement.html', {'content': text}, RequestContext(request))


def contacts(request):
    text = "<address>Организатор мероприятия<br> <i class='icon-envelope'></i> Константинов Евгений Сергеевич<br> jskonst@yandex.ru</address> <br>"
    return render_to_response('contact.html', {'content': text}, RequestContext(request))


def schedule(request):
    staticfile = settings.STATIC_ROOT + "progr.html"
    info = open(staticfile)
    text = info.read()
    info.close()
    return render_to_response('schedule.html', {'content': text}, RequestContext(request))


def news(request):
    newsDir = settings.STATIC_ROOT + "news/"
    text = []
    fileNames = glob.glob(newsDir + '*.html')
    fileNames.sort()
    fileNames.reverse()  # sort()
    for i in fileNames:
        info = open(i)
        text.append(info.read())  # читаем содержимое файла и добавляем его к списку
        info.close()
    #выводим на страницу
    # Делим на страницы
    paginator = Paginator(text, 1)
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        news = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        news = paginator.page(paginator.num_pages)
    return render_to_response('news.html', {'items': news}, RequestContext(request))
