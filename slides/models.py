# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Presenter(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    position = models.CharField(max_length=50)
    contact_email = models.EmailField(max_length=50)
    image = models.ImageField(upload_to='presenter')
    last_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '%s' % (self.name)

class Event(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    last_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to = 'events')
    presenter = models.ForeignKey(
        Presenter,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return '%s' % (self.name)


