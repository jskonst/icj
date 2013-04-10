# -*- coding=utf8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from forms import UserProfileForm, UserForm
from models import UserProfile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def profile(request):
    user = request.user
    if user.is_authenticated():
        profile = user.get_profile()
        if request.method == 'POST':
            profileForm = UserProfileForm(request.POST, instance=profile)
            userForm = UserForm(request.POST, instance=user)
            if profileForm.is_valid() and userForm.is_valid():
                profileForm.save()
                userForm.save()
        else:
            profileForm = UserProfileForm(instance=profile)
            userForm = UserForm(instance=user)

        return render_to_response('registration/profile.html', {'form': profileForm, 'myUser': userForm}, context_instance=RequestContext(request))
    else:
        # Перенаправляем на страницу входа
        return HttpResponseRedirect('/accounts/login/')


def userlist(request):
    profiles = UserProfile.objects.all()
    # Теперь для каждого надо получить Фио
    result = []
    for prof in profiles:
        fName = prof.user.first_name
        if fName:
            fName = fName[0] + "."
        lName = prof.user.last_name
        sName = prof.surname
        if sName:
            sName = sName[0] + "."
        name = lName + " " + fName + sName
        if name == " ":
            name = prof.user.username
        result.append({'name': name, 'profile': prof})
    paginator = Paginator(result, 20)
    page = request.GET.get('page')
    try:
        ulist = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        ulist = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        ulist = paginator.page(paginator.num_pages)
    return render_to_response('userlist.html', {'items': ulist}, RequestContext(request))


def userbage(request):
    profiles = UserProfile.objects.all()
    # Теперь для каждого надо получить Фамилию и имя
    result = []
    for prof in profiles:
        fName = prof.user.first_name
        lName = prof.user.last_name
        name = lName + " " + fName
        if name == " ":
            name = prof.user.username
        result.append({'name': name, 'profile': prof})
    paginator = Paginator(result, 100)
    page = request.GET.get('page')
    try:
        ulist = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        ulist = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        ulist = paginator.page(paginator.num_pages)

    return render_to_response('userbage.html', {'items': ulist}, RequestContext(request))
