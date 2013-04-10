# -*- coding=utf8 -*-
from registration.forms import RegistrationFormUniqueEmail
from django import forms
#from django.utils.translation import ugettext_lazy as _
from models import UserProfile
from django.contrib.auth.models import User
#from registration.models import RegistrationProfile


class UserRegistrationForm(RegistrationFormUniqueEmail):
    # Да, здесь повторение кода, надо будет докрутить
    country = forms.CharField(label=u'Страна')
    city = forms.CharField(label=u'Город')
    company = forms.CharField(label=u'Компания/Вуз')
    job = forms.CharField(required=False, label=u'Должность')
    dokladchik = forms.BooleanField(required=False, label=u'Я буду докладчиком (доклады можно добавить в профиле)')
    last_name = forms.CharField(max_length=50, required=False, label=u'Фамилия')
    first_name = forms.CharField(max_length=50, required=False, label=u'Имя')
    surname = forms.CharField(required=False, label=u'Отчество')
    accepted_eula = forms.BooleanField(label=u'Я принимаю условия участия')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('surname', 'country', 'city', 'company', 'job', 'dokladchik', )
        exclude = ('user', )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('last_name', 'first_name')
