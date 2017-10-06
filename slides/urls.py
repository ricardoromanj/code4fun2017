from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<Event_name>[0-9]+)/$', views.EventSlide, name='event'),
]

