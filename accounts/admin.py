# -*- coding=utf8 -*-
from django.contrib import admin
from django.contrib.auth.models import User
from accounts.models import UserProfile
from django.contrib.auth.admin import UserAdmin

# Говорим что у нас будет другая форма регистрации
admin.site.unregister(User)


# Немного магии :)
class UserProfileInline(admin.StackedInline):
    model = UserProfile


# создаем нашу модель отображения
class AccountAdmin(UserAdmin):
    inlines = [UserProfileInline]
    list_display = ('username', 'email', 'is_staff', 'is_active', )

# А вот теперь регистрируем её
admin.site.register(User, AccountAdmin)
