# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context, Template, RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
import datetime
from django.conf import settings
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from datetime import datetime
from django.forms.forms import NON_FIELD_ERRORS
#from apps.accounts.forms import *
from django.views.decorators.cache import cache_control
from django.core import serializers
from django.core.context_processors import csrf


from forms import ProvinciasForm,DepartamentosForm,CiudadesForm,UnidadesForm,DependenciasForm,LicenciaForm,AgrupacionForm,EscalafonForm
from models import RefPaises,RefProvincia,RefDepartamentos,RefCiudades,UnidadesRegionales,Dependencias,RefLicencia,RefAgrupacion,RefEscalafon



@login_required
def pais(request):
  clase = "pais"
  columns = ["descripcion"]
  pais = RefPaises()
  form = PaisesForm()
  if request.method =="POST": 
      form = PaisesForm(request.POST)
      if form.is_valid():
        pais.descripcion = form.cleaned_data['descripcion']
        pais.save()
        form = PaisesForm()
        pais = RefPaises()
  
  lista = RefPaises.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.descripcion+'</td>'
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def edit_pais(request,pais):
  clase="pais"
  columns = ["descripcion"]
  pais = RefPaises.objects.get(id=pais)
  form = PaisesForm(instance=pais)
  if request.method == 'POST':
    form = PaisesForm(request.POST)
    if form.is_valid():
      pais.descripcion = form.cleaned_data['descripcion'];
      pais.save()
      form = PaisesForm()
      pais = RefPaises()

  lista = RefPaises.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.descripcion+'</td>'
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'pais':pais,'tbody':tbody},context_instance=RequestContext(request))  

@login_required
def remove_pais(request,pais):
  clase="pais"
  columns = ["descripcion"]
  pais = RefPaises.objects.get(id=pais)
  try:
     pais.delete()
  except Exception, e:
     raise e 
  form = PaisesForm()
  pais = RefPaises()
  lista = RefPaises.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.descripcion+'</td>'

  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'pais':pais,'tbody':tbody},context_instance=RequestContext(request))  

@login_required
def provincia(request):
  clase = "provincia"
  columns = ["pais","descripcion"]
  provincia = RefProvincia()
  form = ProvinciasForm()
  if request.method == 'POST':
    form = ProvinciasForm(request.POST)
    print form
    if form.is_valid():
      provincia.pais        = form.cleaned_data['pais']
      provincia.descripcion = form.cleaned_data['descripcion']
      provincia.save()
      form = ProvinciasForm()
      provincia = RefProvincia()

  lista = RefProvincia.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.pais.descripcion+'</td><td>'+elemento.descripcion+'</td>'
      

  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'provincia':provincia,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def edit_provincia(request,prov):
  clase="provincia"
  columns = ["pais","descripcion"]
  provincia = RefProvincia.objects.get(id=prov)
  form = ProvinciasForm(instance=provincia)
  if request.method == 'POST':
    form = ProvinciasForm(request.POST)
    if form.is_valid():
      provincia.pais        = form.cleaned_data['pais'];
      provincia.descripcion = form.cleaned_data['descripcion']
      provincia.save()
      form = ProvinciasForm()
      provincia = RefProvincia()

  lista = RefProvincia.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.pais.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'provincia':provincia,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def remove_provincia(request,prov):
  clase="provincia"
  columns = ["pais","descripcion"]
  provincia = RefProvincia.objects.get(id=prov)
  try:
     provincia.delete()
  except Exception, e:
     raise e 
  form = ProvinciasForm()
  provincia = RefProvincia()
  lista = RefProvincia.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.pais.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'provincia':provincia,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def departamento(request):
  clase = "departamento"
  columns = ["provincia","descripcion"]
  departamento = RefDepartamentos()
  form = DepartamentosForm()
  if request.method == 'POST':
    form = DepartamentosForm(request.POST)
    print form
    if form.is_valid():
      departamento.provincia   = form.cleaned_data['provincia']
      departamento.descripcion = form.cleaned_data['descripcion']
      departamento.save()
      form = DepartamentosForm()
      departamento = RefDepartamentos()

  lista = RefDepartamentos.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.provincia.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'departamento':departamento,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def edit_departamento(request,dto):
  clase="departamento"
  columns = ["provincia","descripcion"]
  departamento = RefDepartamentos.objects.get(id=dto)
  form = DepartamentosForm(instance=departamento)
  if request.method == 'POST':
    form = DepartamentosForm(request.POST)
    if form.is_valid():
      departamento.provincia   = form.cleaned_data['provincia'];
      departamento.descripcion = form.cleaned_data['descripcion']
      departamento.save()
      form = DepartamentosForm()
      departamento = RefDepartamentos()

  lista = RefDepartamentos.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.provincia.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'departamento':departamento,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def remove_departamento(request,dto):
  clase="departamento"
  columns = ["provincia","descripcion"]
  departamento = RefDepartamentos.objects.get(id=dto)
  try:
     departamento.delete()
  except Exception, e:
     raise e 
  form = DepartamentosForm()
  departamento = RefDepartamentos()
  lista = RefDepartamentos.objects.all()
 
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.provincia.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'departamento':departamento,'tbody':tbody},context_instance=RequestContext(request))  

@login_required
def ciudad(request):
  clase = "ciudad"
  columns = ["pais","provincia","descripcion"]
  ciudad = RefCiudades()
  form = CiudadesForm()
  if request.method == 'POST':
    form = CiudadesForm(request.POST)
    print form
    if form.is_valid():
      ciudad.pais           = form.cleaned_data['pais']
      ciudad.provincia      = form.cleaned_data['provincia']
      ciudad.departamento   = form.cleaned_data['departamento']
      ciudad.descripcion    = form.cleaned_data['descripcion']
      ciudad.save()
      form = CiudadesForm()
      ciudad = RefCiudades()

  lista = RefCiudades.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.pais.descripcion+'</td><td>'+elemento.provincia.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'ciudad':ciudad,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def edit_ciudad(request,cdd):
  clase="ciudad"
  columns = ["pais","provincia","descripcion"]
  ciudad = RefCiudades.objects.get(id=cdd)
  form = CiudadesForm(instance=ciudad)
  if request.method == 'POST':
    form = CiudadesForm(request.POST)
    if form.is_valid():
      ciudad.pais           = form.cleaned_data['pais']
      ciudad.provincia      = form.cleaned_data['provincia']
      ciudad.departamento   = form.cleaned_data['departamento']
      ciudad.descripcion    = form.cleaned_data['descripcion']
      ciudad.save()
      form = CiudadesForm()
      ciudad = RefCiudades()

  lista = RefCiudades.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.pais.descripcion+'</td><td>'+elemento.provincia.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'ciudad':ciudad,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def remove_ciudad(request,cdd):
  clase="ciudad"
  columns = ["pais","provincia","descripcion"]
  ciudad = RefCiudades.objects.get(id=cdd)
  try:
     ciudad.delete()
  except Exception, e:
     raise e 
  form = CiudadesForm()
  ciudad = RefCiudades()
  lista = RefCiudades.objects.all()
  tbody = []
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.pais.descripcion+'</td><td>'+elemento.provincia.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'ciudad':ciudad,'tbody':tbody},context_instance=RequestContext(request))  


@login_required
def unidad(request):
  clase = "unidad"
  columns = ["ciudad","descripcion"]
  unidad = UnidadesRegionales()
  form = UnidadesForm()
  if request.method == 'POST':
    form = UnidadesForm(request.POST)
    if form.is_valid():
      unidad.ciudad         = form.cleaned_data['ciudad']
      unidad.descripcion    = form.cleaned_data['descripcion']
      unidad.save()
      form = UnidadesForm()
      unidad = UnidadesRegionales()

  lista = UnidadesRegionales.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.ciudad.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'unidad':unidad,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def edit_unidad(request,id):
  clase = "unidad"
  columns = ["ciudad","descripcion"]
  unidad = UnidadesRegionales.objects.get(id=id)
  form = UnidadesForm(instance=unidad)
  if request.method == 'POST':
    form = UnidadesForm(request.POST)
    if form.is_valid():
      unidad.ciudad         = form.cleaned_data['ciudad']
      unidad.descripcion    = form.cleaned_data['descripcion']
      unidad.save()
      form = UnidadesForm()
      unidad = UnidadesRegionales()

  lista = UnidadesRegionales.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.ciudad.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'unidad':unidad,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def remove_unidad(request,id):
  clase = "unidad"
  columns = ["ciudad","descripcion"]
  unidad = UnidadesRegionales.objects.get(id=id)
  try:
     unidad.delete()
  except Exception, e:
     raise e 
  form = UnidadesForm()
  unidad = UnidadesRegionales()
  lista = UnidadesRegionales.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.ciudad.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'unidad':unidad,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def dependencia(request):
  clase = "dependencia"
  columns = ["unidad regional","ciudad","descripcion"]
  dependencia = Dependencias()
  form = DependenciasForm()
  if request.method == 'POST':
    form = DependenciasForm(request.POST)
    if form.is_valid():
      dependencia.unidades_regionales = form.cleaned_data['unidades_regionales']
      dependencia.ciudad              = form.cleaned_data['ciudad']
      dependencia.descripcion         = form.cleaned_data['descripcion']
      dependencia.save()
      form = DependenciasForm()
      dependencia = Dependencias()

  lista = Dependencias.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.unidades_regionales.descripcion+'</td><td>'+elemento.ciudad.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'dependencia':dependencia,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def edit_dependencia(request,id):
  clase = "dependencia"
  columns = ["unidad regional","ciudad","descripcion"]
  dependencia = Dependencias.objects.get(id=id)
  form = DependenciasForm(instance=dependencia)
  if request.method == 'POST':
    form = DependenciasForm(request.POST)
    if form.is_valid():
      dependencia.unidades_regionales = form.cleaned_data['unidades_regionales']
      dependencia.ciudad              = form.cleaned_data['ciudad']
      dependencia.descripcion         = form.cleaned_data['descripcion']
      dependencia.save()
      form = DependenciasForm()
      dependencia = Dependencias()

  lista = Dependencias.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.unidades_regionales.descripcion+'</td><td>'+elemento.ciudad.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'dependencia':dependencia,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def remove_dependencia(request,id):
  clase = "dependencia"
  columns = ["unidad regional","ciudad","descripcion"]
  dependencia = Dependencias.objects.get(id=id)
  try:
     dependencia.delete()
  except Exception, e:
     raise e 
  form = DependenciasForm()
  dependencia = Dependencias()
  lista = Dependencias.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.unidades_regionales.descripcion+'</td><td>'+elemento.ciudad.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'dependencia':dependencia,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def licencia(request):
  clase = "licencia"
  columns = ["codigo","descripcion"]
  licencia = RefLicencia()
  form = LicenciaForm()
  if request.method == 'POST':
    form = LicenciaForm(request.POST)
    if form.is_valid():
      licencia.codigo 				= form.cleaned_data['codigo']
      licencia.descripcion         	= form.cleaned_data['descripcion']
      licencia.save()
      form = LicenciaForm()
      licencia = RefLicencia()

  lista = RefLicencia.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.codigo+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'licencia':licencia,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def edit_licencia(request,id):
  clase = "licencia"
  columns = ["codigo","descripcion"]
  licencia = RefLicencia.objects.get(id=id)
  form = LicenciaForm(instance=licencia)
  if request.method == 'POST':
    form = LicenciaForm(request.POST)
    if form.is_valid():
      licencia.codigo 				= form.cleaned_data['codigo']
      licencia.descripcion         	= form.cleaned_data['descripcion']
      licencia.save()
      form = LicenciaForm()
      licencia = RefLicencia()

  lista = RefLicencia.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.codigo+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'licencia':licencia,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def remove_licencia(request,id):
  clase = "licencia"
  columns = ["codigo","descripcion"]
  licencia = RefLicencia.objects.get(id=id)
  try:
     licencia.delete()
  except Exception, e:
     raise e 
  form = LicenciaForm()
  licencia = RefLicencia()
  lista = RefLicencia.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.codigo+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'licencia':licencia,'tbody':tbody},context_instance=RequestContext(request))


@login_required
def agrupacion(request):
  clase = "agrupacion"
  columns = ["descripcion"]
  agrupacion = RefAgrupacion()
  form = AgrupacionForm()
  if request.method == 'POST':
    form = AgrupacionForm(request.POST)
    if form.is_valid():
      agrupacion.descripcion          = form.cleaned_data['descripcion']
      agrupacion.save()
      form = AgrupacionForm()
      agrupacion = RefAgrupacion()

  lista = RefAgrupacion.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.descripcion+'</td>'
  
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'agrupacion':agrupacion,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def edit_agrupacion(request,id):
  clase = "agrupacion"
  columns = ["descripcion"]
  agrupacion = RefAgrupacion.objects.get(id=id)
  form = AgrupacionForm(instance=agrupacion)
  if request.method == 'POST':
    form = AgrupacionForm(request.POST)
    if form.is_valid():
      agrupacion.descripcion          = form.cleaned_data['descripcion']
      agrupacion.save()
      form = AgrupacionForm()
      agrupacion = RefAgrupacion()

  lista = RefAgrupacion.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.descripcion+'</td>'
  
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'agrupacion':agrupacion,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def remove_agrupacion(request,id):
  clase = "agrupacion"
  columns = ["descripcion"]
  agrupacion = RefAgrupacion.objects.get(id=id)
  try:
     agrupacion.delete()
  except Exception, e:
     raise e 
  form = AgrupacionForm()
  agrupacion = RefAgrupacion()
  lista = RefAgrupacion.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.descripcion+'</td>'
  
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'agrupacion':agrupacion,'tbody':tbody},context_instance=RequestContext(request))


@login_required
def escalafon(request):
  clase = "escalafon"
  columns = ["agrupacion","descripcion"]
  escalafon = RefEscalafon()
  form = EscalafonForm()
  if request.method == 'POST':
    form = EscalafonForm(request.POST)
    if form.is_valid():
      escalafon.agrupacion        = form.cleaned_data['agrupacion']
      escalafon.descripcion       = form.cleaned_data['descripcion']
      escalafon.save()
      form = EscalafonForm()
      escalafon = RefEscalafon()

  lista = RefEscalafon.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.agrupacion.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'escalafon':escalafon,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def edit_escalafon(request,id):
  clase = "escalafon"
  columns = ["agrupacion","descripcion"]
  escalafon = RefEscalafon.objects.get(id=id)
  form = EscalafonForm(instance=escalafon)
  if request.method == 'POST':
    form = EscalafonForm(request.POST)
    if form.is_valid():
      escalafon.agrupacion        = form.cleaned_data['agrupacion']
      escalafon.descripcion       = form.cleaned_data['descripcion']
      escalafon.save()
      form = EscalafonForm()
      escalafon = RefEscalafon()

  lista = RefEscalafon.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.agrupacion.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'escalafon':escalafon,'tbody':tbody},context_instance=RequestContext(request))

@login_required
def remove_escalafon(request,id):
  clase = "escalafon"
  columns = ["agrupacion","descripcion"]
  escalafon = RefEscalafon.objects.get(id=id)
  print escalafon
  try:
     escalafon.delete()
  except Exception, e:
     raise e 
  form = EscalafonForm()
  escalafon = RefEscalafon()
  lista = RefEscalafon.objects.all()
  tbody = {}
  for elemento in lista:

      tbody[elemento.id] = '<td>'+elemento.agrupacion.descripcion+'</td><td>'+elemento.descripcion+'</td>'
  
  return render_to_response('referencias/abm.html',{'form':form,'lista':lista,'clase':clase,"columns":columns,'escalafon':escalafon,'tbody':tbody},context_instance=RequestContext(request))