#-*- coding=utf8 -*-
from django.db import models
from accounts.models import UserProfile
# Create your models here.


class Section(models.Model):
    section = models.CharField(max_length=100, verbose_name=u'Название секции')

    def __unicode__(self):
        return self.section


class Doklad(models.Model):
    section = models.ForeignKey(Section)
    title = models.CharField(max_length=1024, verbose_name=u'Назвние доклада')
    authors = models.CharField(max_length=1024, blank=True, verbose_name=u'Соавторы')
    author = models.ManyToManyField(UserProfile, blank=True)
    text = models.TextField(verbose_name=u'Текст доклада (можно использовать HTML разметку, заголовки не выше h3)')
    publish = models.BooleanField(blank=True, verbose_name=u'Опубликовать')

    def __unicode__(self):
        return self.title
