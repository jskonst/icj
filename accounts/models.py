# -*- coding=utf8 -*-

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class UserProfile(models.Model):
    # Обязательно поле для расширения модели
    user = models.OneToOneField(User, unique=True, primary_key=True)
    #Остальные, расширенные поля модели
    # Обязательные
    #Страна
    country = models.CharField(max_length=100, verbose_name=u'Страна')
    #Город
    city = models.CharField(max_length=100, verbose_name=u'Город')
    #Компания/Вуз
    company = models.CharField(max_length=100, verbose_name=u'Компания/Вуз')
    #Роль: докладчик/слушатель
    dokladchik = models.BooleanField(blank=True, verbose_name=u'Я буду докладчиком (доклады можно добавить в профиле)')
    #Для докладчиков:
    #Фамилия
    #Имя
    surname = models.CharField(max_length=30, blank=True, verbose_name=u'Отчество')
        #Отчество
        #(Крайне желательно для формирования сборника тезисов и обращения при выступлении)
        #Должность
    job = models.CharField(max_length=200, blank=True, verbose_name=u'Должность')
    # Условия соглашения принял
    accepted_eula = models.BooleanField(verbose_name=u'Я принимаю условия участия')
    #objects = UserManager()

    def __unicode__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)
