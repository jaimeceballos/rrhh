#! /usr/bin/python	
# -*- encoding: utf-8 -*-
from django.conf.urls import patterns, include, url
from views import *


urlpatterns = patterns('',
	url(r'^pais/$',  pais, name='pais'),
	url(r'^edit_pais/(?P<pais>[0-9A-Za-z]+)/$', edit_pais ,name='edit_pais'),
	url(r'^remove_pais/(?P<pais>[0-9A-Za-z]+)/$', remove_pais ,name='remove_pais'),
	
	url(r'^provincia/$',  provincia, name='provincia'),
	url(r'^edit_provincia/(?P<prov>[0-9A-Za-z]+)/$', edit_provincia ,name='edit_provincia'),
	url(r'^remove_provincia/(?P<prov>[0-9A-Za-z]+)/$', remove_provincia ,name='remove_provincia'),
	
	url(r'^departamento/$',  departamento, name='departamento'),
	url(r'^edit_departamento/(?P<dto>[0-9A-Za-z]+)/$', edit_departamento ,name='edit_departamento'),
	url(r'^remove_departamento/(?P<dto>[0-9A-Za-z]+)/$', remove_departamento ,name='remove_departamento'),
	
	url(r'^ciudad/$',  ciudad, name='ciudad'),
	url(r'^edit_ciudad/(?P<cdd>[0-9A-Za-z]+)/$', edit_ciudad ,name='edit_ciudad'),
	url(r'^remove_ciudad/(?P<cdd>[0-9A-Za-z]+)/$', remove_ciudad ,name='remove_ciudad'),
	
	url(r'^unidad/$',  unidad, name='unidad'),
	url(r'^edit_unidad/(?P<id>[0-9A-Za-z]+)/$', edit_unidad ,name='edit_unidad'),
	url(r'^remove_unidad/(?P<id>[0-9A-Za-z]+)/$', remove_unidad ,name='remove_unidad'),
	
	url(r'^dependencia/$',  dependencia, name='dependencia'),
	url(r'^edit_dependencia/(?P<id>[0-9A-Za-z]+)/$', edit_dependencia ,name='edit_dependencia'),
	url(r'^remove_dependencia/(?P<id>[0-9A-Za-z]+)/$', remove_dependencia ,name='remove_dependencia'),

	url(r'^licencia/$',  licencia, name='licencia'),
	url(r'^edit_licencia/(?P<id>[0-9A-Za-z]+)/$', edit_licencia ,name='edit_licencia'),
	url(r'^remove_licencia/(?P<id>[0-9A-Za-z]+)/$', remove_licencia ,name='remove_licencia'),

	url(r'^agrupacion/$',  agrupacion, name='agrupacion'),
	url(r'^edit_agrupacion/(?P<id>[0-9A-Za-z]+)/$', edit_agrupacion ,name='edit_agrupacion'),
	url(r'^remove_agrupacion/(?P<id>[0-9A-Za-z]+)/$', remove_agrupacion ,name='remove_agrupacion'),

	url(r'^escalafon/$',  escalafon, name='escalafon'),
	url(r'^edit_escalafon/(?P<id>[0-9A-Za-z]+)/$', edit_escalafon ,name='edit_escalafon'),
	url(r'^remove_escalafon/(?P<id>[0-9A-Za-z]+)/$', remove_escalafon ,name='remove_escalafon'),

)