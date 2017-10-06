# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import datetime
from slides.models import Event, Presenter 

def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events })

def events(request):
    return render(request, 'events.html', {'events': events })
