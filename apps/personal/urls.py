#! /usr/bin/python
# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from views import *

urlpatterns=patterns( '',  
  url(r'^$',  home, name='home'),
  url(r'^nuevo/', alta_personal, name='alta_personal'),
  url(r'^editar/(?P<id>[0-9A-Za-z]+)/$', editar_personal, name='editar_personal'),
  url(r'^borrar/(?P<id>[0-9A-Za-z]+)/$', remove_personal, name='remove_personal'),

 )