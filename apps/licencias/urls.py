#! /usr/bin/python
# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from views import *

urlpatterns=patterns( '',  
  url(r'^$',  licencias, name='licencias'),

 )