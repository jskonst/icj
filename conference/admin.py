# -*- coding=utf8 -*-
from django.contrib import admin
from conference.models import Section, Doklad


class SectionAdmin(admin.ModelAdmin):
    list_display = ('section', )


class DokladAdmin(admin.ModelAdmin):
    list_display = ('section', 'title', 'authors', 'text', )
# А вот теперь регистрируем их
admin.site.register(Section, SectionAdmin)
admin.site.register(Doklad, DokladAdmin)
