# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from slides.models import Event, Presenter

class EventAdmin(admin.ModelAdmin):
        pass

class PresenterAdmin(admin.ModelAdmin):
        pass

#class PresentationAdmin(admin.ModelAdmin):
#    model = Presentation 
#    list_display = ['name', ]
#    inlines = [SlideInline]


admin.site.register(Event, EventAdmin)
admin.site.register(Presenter, PresenterAdmin)
