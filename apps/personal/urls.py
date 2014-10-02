#! /usr/bin/python
# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from views import *

urlpatterns=patterns( '',  
  url(r'^$',  home, name='home'),
  url(r'^nuevo/', alta_personal, name='alta_personal'),

 )