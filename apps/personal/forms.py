#! /usr/bin/python
# -*- encoding: utf-8 -*-

from django import forms 
from apps.referencias.models import *
from apps.personal.models import *
from django.forms import ModelForm, TimeField
from django.contrib import admin
from django.utils import timezone 
from django.conf import settings
from django.contrib.auth.models import  Group,Permission,User
from django.contrib.admin import widgets
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms.widgets import CheckboxSelectMultiple
from django.core.exceptions import ValidationError

class PersonasForm(forms.ModelForm):
    apellidos = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Apellido/s','required':'required'})),required=True)
    nombres =  forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre/s','required':'required'})),required=True)
    tipo_doc = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level','required':'required'})),queryset=RefTipoDocumento.objects.all()) 
    nro_doc = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Numero de documento','required':'required'})),required=True)
    ciudad_nac = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'select','required':'required'})),queryset=RefCiudades.objects.filter(pais=RefPaises.objects.filter(descripcion__contains='ARGENTINA').values('id')))
    ciudad_res = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'select','required':'required'})),queryset=RefCiudades.objects.filter(pais=RefPaises.objects.filter(descripcion__contains='ARGENTINA').values('id')))
    sexo_id = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level','required':'required'})),queryset=RefSexo.objects.all()) 
    fecha_nac = forms.DateField(widget=forms.DateInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Fecha de nacimiento','required':'required','readonly':'readonly'})),required=True)
    estado_civil =  forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level','required':'required'})),queryset=RefEstadosciv.objects.all())
    
    def __init__(self, *args, **kwargs):
            super(ModelForm, self).__init__(*args, **kwargs)
            self.fields['fecha_nac'].widget.format = '%d/%m/%Y'

            # at the same time, set the input format on the date field like you want it:
            self.fields['fecha_nac'].input_formats = ['%d/%m/%Y']
   
    class Meta:
        model = Personas
        exclude = ('pais_nac','ocupacion','cuit','celular','alias')
        

class PersonalForm(forms.ModelForm):
    legajo = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Legajo','required':'required'})),required=True)
    fecha_ingreso = forms.DateField(widget=forms.DateInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Fecha de ingreso','required':'required','readonly':'readonly'})),required=True)
    ant_otro_organismo = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Antiguedad reconocida de otros organismos','required':'required'})),required=True)
    escalafon = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'select','required':'required'})),queryset=RefEscalafon.objects.all())


    def __init__(self, *args, **kwargs):
            super(ModelForm, self).__init__(*args, **kwargs)
            self.fields['fecha_ingreso'].widget.format = '%d/%m/%Y'

            # at the same time, set the input format on the date field like you want it:
            self.fields['fecha_ingreso'].input_formats = ['%d/%m/%Y']

    class Meta:
        model = Personal
        exclude = ('persona_id','credencial','nro_cuenta_bco','nro_seros')