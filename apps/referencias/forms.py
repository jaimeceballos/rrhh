#! /usr/bin/python
# -*- encoding: utf-8 -*-

from django import forms 
from apps.referencias.models import *
from django.forms import ModelForm, TimeField
from django.contrib import admin
from django.utils import timezone 
from django.conf import settings
from django.contrib.auth.models import  Group,Permission,User
from django.contrib.admin import widgets
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms.widgets import CheckboxSelectMultiple
from django.core.exceptions import ValidationError

class PaisesForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre del Pais','required':'required'})),required=True)
    class Meta:
        model = RefPaises

class ProvinciasForm(forms.ModelForm):
    pais        = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level','required':'required'})),queryset=RefPaises.objects.all())
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre de la Provincia','required':'required','autocomplete':'off'})),required=True)
   
    class Meta:
        model = RefProvincia

class DepartamentosForm(forms.ModelForm):
    provincia   = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level','required':'required'})),queryset=RefProvincia.objects.filter(pais=RefPaises.objects.filter(descripcion__contains="ARGENTINA").values('id')))
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre del Departamento','required':'required','autocomplete':'off'})),required=True)

    class Meta:
        model = RefDepartamentos

class CiudadesForm(forms.ModelForm):
    pais            = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level','required':'required'})),queryset=RefPaises.objects.all())
    provincia       = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})),queryset=RefProvincia.objects.all(),required=False)
    departamento    = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})),queryset=RefDepartamentos.objects.all(),required=False)
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre de la ciudad','required':'required','autocomplete':'off'})),required=True)

    class Meta:
        model = RefCiudades
        exclude = ('lat','longi',)

class UnidadesForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre de la unidad','required':'required','autocomplete':'off'})),required=True)
    ciudad = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= RefCiudades.objects.filter(provincia = RefProvincia.objects.filter(descripcion__contains = 'CHUBUT').values('id'))  )
    class Meta:
        model = UnidadesRegionales

class DependenciasForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Nombre de la dependencia','required':'required','autocomplete':'off'})),required=True)
    ciudad = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= RefCiudades.objects.filter(provincia = RefProvincia.objects.filter(descripcion__contains = 'CHUBUT').values('id'))  )
    unidades_regionales = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= UnidadesRegionales.objects.all())

    
    class Meta:
        model = Dependencias 

class OcupacionForm(forms.ModelForm):

    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Ocupación / Profesión / Oficio','required':'required','autocomplete':'off'})),required=True)
    class Meta:
        model = RefOcupacion


class SexoForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Sexo','required':'required'})),required=True)
    class Meta:
        model = RefSexo

class TipoDocumentoForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Tipo de documento','required':'required'})),required=True)
    class Meta:
        model = RefTipoDocumento 

class EstadoCivilForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Estado civil','required':'required'})),required=True)
    class Meta:
        model = RefEstadosciv 

class TipoJerarquiaForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Tipo Jerarquia','required':'required'})),required=True)
 
    class Meta:
        model = RefTipoJerarquia
 
class DivisionJerarquiaForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Division Jerarquia','required':'required'})),required=True)
 
    class Meta:
        model = RefDivisionJerarquia
 
class JerarquiasForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Jerarquia','required':'required'})),required=True)
    ref_tipo_jerarquia = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= RefTipoJerarquia.objects.all())
    ref_division_jerarquia = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level'})), queryset= RefDivisionJerarquia.objects.all())
 
    class Meta:
        model = RefJerarquias

class LicenciaForm(forms.ModelForm):
    codigo = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Codigo de licencia','required':'required'})),required=True)
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Descripcion','required':'required'})),required=True)

    class Meta:
        model = RefLicencia


class AgrupacionForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Descripcion','required':'required'})),required=True)

    class Meta:
        model = RefAgrupacion

class EscalafonForm(forms.ModelForm):
    agrupacion = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-block-level','required':'required'})), queryset= RefAgrupacion.objects.all())
    descripcion = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control input-block-level', 'placeholder':'Descripcion','required':'required'})),required=True)

    class Meta:
        model = RefEscalafon