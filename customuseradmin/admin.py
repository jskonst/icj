# -*- coding:utf-8 -*-
#Модуль необходим для того, чтобы в админке показывать 
# Активирован пользователь или нет
from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin    

admin.site.unregister(User)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff','is_active',)
    list_filter = ('is_staff', 'is_superuser', 'is_active',)    
admin.site.register(User, CustomUserAdmin)
