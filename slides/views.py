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
