# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from slides.models import EventSlide, CalendarSlide, BioSlide, Presentation, Slide

class EventSlideAdmin(admin.ModelAdmin):
        pass

class CalendarSlideAdmin(admin.ModelAdmin):
        pass

class BioSlideAdmin(admin.ModelAdmin):
        pass

class SlideInline(admin.TabularInline):
    model = Slide 
    fk_name = 'presentation'

class PresentationAdmin(admin.ModelAdmin):
    model = Presentation 
    list_display = ['name', ]
    inlines = [SlideInline]


admin.site.register(EventSlide, EventSlideAdmin)
admin.site.register(CalendarSlide, CalendarSlideAdmin)
admin.site.register(BioSlide, BioSlideAdmin)
admin.site.register(Presentation, PresentationAdmin)
