# -*- coding=utf8 -*-
from models import Doklad, Section
from django import forms


class DokladForm(forms.ModelForm):
    section = forms.ModelChoiceField(queryset=Section.objects.all(), label=u'Секция', empty_label=None)

    class Meta:
        model = Doklad
        #fields = {'section', }
        exclude = ('author')


class DokladListForm(forms.Form):
    # Передаем дополнительным параметром профиль пользователя
    # Чтобы выводить информацию только о его докладах
    def __init__(self, profile, *args, **kwargs):
        super(DokladListForm, self).__init__(*args, **kwargs)
        self.fields['dokList'].queryset = Doklad.objects.filter(author=profile)

    dokList = forms.ModelChoiceField(queryset=Doklad.objects.none(), required=False, label=u'Список докладов', empty_label=None)
