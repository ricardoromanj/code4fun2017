# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import EventSlide

# Create your views here.
def index(request):
    return HttpResponse("Hello World Slides")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>Today: %s.</body></html>" % now
    return HttpResponse(html)

def EventSlide(request):
    Event_list = EventSlide.objects.order_by('-pub_date')[:5]
    return render(request, 'EventSlide/index.html', Presentation.objects.select_related(
   'Presentation.name).all().order_by('-last_updated'))