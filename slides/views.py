# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from slides.models import Event, Presenter 
import json


def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events })

def events(request):
    events = Event.objects.all()
    data = []
    for event in events:
        data = data + [{'title': event.name, 'start': str(event.start), 'end': str(event.end)}]
    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')

def last_updated(request):
    last_updated=None
    events = Event.objects.all()
    for event in events:
        if last_updated == None:
            last_updated = event.last_updated
        else:
            if last_updated < event.last_updated:
                last_updated = event.last_updated
    presenters = Presenter.objects.all()
    for presenter in presenters:
        if last_updated == None:
            last_updated = presenter.last_updated
        else: 
            if last_updated < presenter.last_updated:
                last_updated = presenter.last_updated
    data = json.dumps({'last_updated': str(last_updated)})
    return HttpResponse(data, content_type='application/json')

