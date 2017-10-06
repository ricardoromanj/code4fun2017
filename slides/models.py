# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Slide(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    contact_email = models.EmailField(max_length=50)

class Event(Slide):
    location = models.CharField(max_length=50)
    date = models.DateTimeField()

class Bio(Slide):
    image = models.ImageField(upload_to = 'images')
#class Calendar(models.Model):
