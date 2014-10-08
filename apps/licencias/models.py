#! /usr/bin/python
# -*- encoding: utf-8 -*-|

from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import Group,Permission,User
from django.db.models import signals
from apps.referencias.models import *
from apps.personal.models import *

class Licencia(models.Model):
	personal 		= models.ForeignKey('personal.Personal',related_name='licencias',on_delete=models.PROTECT)
	codigo 			= models.ForeignKey('referencias.RefLicencia',on_delete=models.PROTECT)
	fecha_desde 	= models.DateField()
	cantidad_dias 	= models.IntegerField()
	fecha_hasta 	= models.DateField()
	observaciones 	= models.CharField(max_length = 150,blank =True, null =True)

	class Meta:
		unique_together = ('personal','codigo','fecha_desde','cantidad_dias')
		ordering 		= ['-fecha_desde']
		db_table		= 'Licencia'

