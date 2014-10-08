#! /usr/bin/python
# -*- encoding: utf-8 -*-

from django import forms 
from apps.referencias.models import *
from apps.licencias.models import *
from django.forms import ModelForm, TimeField
from django.contrib import admin
from django.utils import timezone 
from django.conf import settings
from django.contrib.auth.models import  Group,Permission,User
from django.contrib.admin import widgets
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms.widgets import CheckboxSelectMultiple
from django.core.exceptions import ValidationError


class LicenciaForm(forms.ModelForm):
	personal	= forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'select','required':'required'})),queryset=Personal.objects.filter(borrado=False),label="DNI Empleado")
	codigo		= forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'select','required':'required'})),queryset=RefLicencia.objects.all(),label="Código de licencia")
	fecha_desde = forms.DateField(widget=forms.DateInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Fecha inicio Licencia','required':'required','readonly':'readonly'})),required=True)
	cantidad_dias = forms.IntegerField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Total de dias de Licencia','required':'required'})),required=True)
	fecha_hasta = forms.DateField(widget=forms.DateInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Fecha de fin de la licencia','required':'required','readonly':'readonly'})),required=True)
	observaciones = forms.CharField(widget=forms.Textarea(attrs=dict({'class':'form-control input-block-level','rows':'4','cols':'50'})))

	def __init__(self, *args, **kwargs):
            super(ModelForm, self).__init__(*args, **kwargs)
            self.fields['fecha_desde'].widget.format = '%d/%m/%Y'
            self.fields['fecha_hasta'].widget.format = '%d/%m/%Y'
            # at the same time, set the input format on the date field like you want it:
            self.fields['fecha_desde'].input_formats = ['%d/%m/%Y']
            self.fields['fecha_hasta'].input_formats = ['%d/%m/%Y']

	class Meta:
		model = Licencia