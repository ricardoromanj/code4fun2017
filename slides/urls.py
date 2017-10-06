from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^events/$', views.events, name='events'),
    url(r'^last_updated/$', views.last_updated, name='last_updated'),
]

