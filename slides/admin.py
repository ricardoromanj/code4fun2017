# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from slides.models import Event, Bio

class EventAdmin(admin.ModelAdmin):
        pass

class BioAdmin(admin.ModelAdmin):
        pass

admin.site.register(Event, EventAdmin)
admin.site.register(Bio, BioAdmin)
