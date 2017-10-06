# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Presentation(models.Model):
    name = models.CharField(max_length=40)
    last_updated = models.DateTimeField(auto_now=True)

# Slides
class Slide(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    contact_email = models.EmailField(max_length=50)
    presentation = models.ForeignKey(
        Presentation,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return '%s' % (self.name)

class CalendarSlide(Slide):
    pass

class EventSlide(Slide):
    location = models.CharField(max_length=50)
    start = models.DateTimeField()
    end = models.DateTimeField()
    calendar = models.ForeignKey(CalendarSlide)

class BioSlide(Slide):
    image = models.ImageField(upload_to = 'images')

