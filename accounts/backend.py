# -*- coding: utf-8 -*-
from django.contrib.sites.models import RequestSite, Site
from registration.backends.default import DefaultBackend
from registration.models import RegistrationProfile
from accounts.models import UserProfile
from django.contrib.auth.models import User


# Бэкэнд регистрации
class RegBackend(DefaultBackend):
    def register(self, request, **kwargs):
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
        print site
        user = User()
        user.username = kwargs['username']
        user.email = kwargs['email']
        password = kwargs['password1']
        user.set_password(password)
        user.first_name = kwargs['first_name']
        user.last_name = kwargs['last_name']
        user.is_active = False
        user.save()
        profile_user = UserProfile()
        # Любое совпадение наименования полей и аргументов- случайно :), так
        # проще не ошибиться
        profile_user.country = kwargs['country']
        profile_user.city = kwargs['city']
        profile_user.company = kwargs['company']
        profile_user.dokladchik = kwargs['dokladchik']
        profile_user.surname = kwargs['surname']
        profile_user.job = kwargs['job']
        profile_user.accepted_eula = kwargs['accepted_eula']
        profile_user.user = user
        profile_user.save()
        prof = RegistrationProfile.objects.create_profile(user)
        prof.send_activation_email(site)
        return user
