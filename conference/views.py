# -*- coding=utf8 -*-
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from conference.forms import DokladForm, DokladListForm
from models import Section, Doklad
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def DokladEdit(request):
    user = request.user
    if user.is_authenticated():
        profile = user.get_profile()
        # необходимо проверить - а установлено ли у него то, что он докладчик
        if profile.dokladchik:
            if request.method == 'POST':
                if 'form_data' in request.session:
                    doklad = request.session['form_data']
                    dokladForm = DokladForm(request.POST, instance=doklad)
                else:
                    doklad = Doklad()
                    dokladForm = DokladForm(request.POST)

                if dokladForm.is_valid():
                    # Создадим новый доклад и сохраним его
                    doklad.section = dokladForm.cleaned_data['section']
                    doklad.title = dokladForm.cleaned_data['title']
                    doklad.authors = dokladForm.cleaned_data['authors']
                    doklad.text = dokladForm.cleaned_data['text']
                    doklad.publish = dokladForm.cleaned_data['publish']
                    doklad.save()
                    doklad.author.add(profile)
                    return HttpResponseRedirect('/accounts/profile/dokladlist')

            else:
                if 'form_data' in request.session:
                    dokladForm = DokladForm(instance=request.session['form_data'])
                else:
                    dokladForm = DokladForm()

            return render_to_response('dokladedit.html', {'title': "Редактировать доклад", 'form': dokladForm}, context_instance=RequestContext(request))
        else:
            # Редиректим на профиль
            return HttpResponseRedirect('/accounts/profile/')
    else:
        # Перенаправляем на страницу входа
        return HttpResponseRedirect('/accounts/login/')


# отображаем список докладов пользователя
def DokladList(request):
    # Удалим сессию, если таковая была (чтоб новые)
    if 'form_data' in request.session:
        del request.session['form_data']
    user = request.user
    if user.is_authenticated():
        profile = user.get_profile()
        # необходимо проверить - а установлено ли у него то, что он докладчик
        if profile.dokladchik:
            if request.method == 'POST':
                dokladForm = DokladListForm(profile, request.POST)
                if dokladForm.is_valid():
                    selected_doc = dokladForm.cleaned_data['dokList']
                    if selected_doc:
                        # мы передаем доклад пользователя
                        request.session['form_data'] = selected_doc
                        return redirect('/accounts/profile/dokladedit')
            else:
                dokladForm = DokladListForm(profile, request.POST)
            return render_to_response('dokladlist.html', {'form': dokladForm}, context_instance=RequestContext(request))
        else:
            # Редиректим на профиль
            return HttpResponseRedirect('/accounts/profile/')
    else:
        # Перенаправляем на страницу входа
        return HttpResponseRedirect('/accounts/login/')


def ShowSection(request):
    id = request.GET.get('id')
    section = Section.objects.get(pk=id)
    # теперь надо сделать выборку
    doklads = Doklad.objects.filter(publish=True, section=section)
    # Теперь для каждого доклада надо получить Фио
    result = []
    for item in doklads:
        authProfile = item.author.get()
        fName = authProfile.user.first_name
        if fName:
            fName = fName[0] + "."
        lName = authProfile.user.last_name
        sName = authProfile.surname
        if sName:
            sName = sName[0] + "."
        name = lName + " " + fName + sName
        if name == " ":
            name = authProfile.user.username
        result.append({'name': name, 'doklad': item, 'profile': authProfile})

    paginator = Paginator(result, 5)
    page = request.GET.get('page')
    try:
        dokl = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        dokl = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        dokl = paginator.page(paginator.num_pages)
    return render_to_response('section_output.html', {'items': dokl, 'section': section, 'variables': section}, context_instance=RequestContext(request))
