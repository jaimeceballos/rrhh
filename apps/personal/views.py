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
from forms import *
from models import *
from django.views.decorators.cache import cache_control
from django.core import serializers
from django.core.context_processors import csrf 




def home(request):

	values={
		
	}
	return render_to_response('base.html',values, context_instance = RequestContext(request))	

def alta_personal(request):
	form 			= PersonalForm()
	form_persona 	= PersonasForm()
	persona 		= Personas()
	personal 		= Personal()
	if request.method == 'POST':
		form = PersonalForm(request.POST)
		form_persona = PersonasForm(request.POST)
		print form_persona.errors
		#print form_persona.is_valid()
		if form.is_valid() and form_persona.is_valid():
			persona.nombres 			= form_persona.cleaned_data['nombres']
			persona.apellidos 			= form_persona.cleaned_data['apellidos']
			persona.tipo_doc 			= form_persona.cleaned_data['tipo_doc']
			persona.nro_doc 			= form_persona.cleaned_data['nro_doc']
			persona.fecha_nac 			= form_persona.cleaned_data['fecha_nac']
			persona.sexo_id 			= form_persona.cleaned_data['sexo_id']
			persona.ciudad_nac 			= form_persona.cleaned_data['ciudad_nac']
			persona.pais_nac			= persona.ciudad_nac.pais
			persona.ciudad_res 			= form_persona.cleaned_data['ciudad_res']
			persona.estado_civil 		= form_persona.cleaned_data['estado_civil']

			personal.legajo 			= form.cleaned_data['legajo']
			personal.fecha_ingreso		= form.cleaned_data['fecha_ingreso']
			personal.ant_otro_organismo	= form.cleaned_data['ant_otro_organismo']
			personal.escalafon			= form.cleaned_data['escalafon']
			personal.credencial			= 0

			try:
				persona.save()
				personal.persona_id = persona
				personal.save()
				form 			= PersonalForm()
				form_persona 	= PersonasForm()
				persona 		= Personas()
				personal 		= Personal()
			except Exception, e:
				raise e


	lista 			= Personal.objects.filter(borrado=False)
	return render_to_response('personal/abm.html',{'form':form,'personal':personal,'form_persona':form_persona,'persona':persona,'lista':lista},context_instance=RequestContext(request))

def editar_personal(request,id):
	personal 		= Personal.objects.get(id=id)
	persona 		= personal.persona_id
	form 			= PersonalForm(instance=personal)
	form_persona 	= PersonasForm(instance=persona)
	if request.method == 'POST':
		form 			= PersonalForm(request.POST)
		form_persona 	= PersonasForm(request.POST)
		print persona
		print form_persona
		if form.is_valid():
			persona.nombres 			= form_persona.cleaned_data['nombres']
			persona.apellidos 			= form_persona.cleaned_data['apellidos']
			persona.tipo_doc 			= form_persona.cleaned_data['tipo_doc']
			persona.nro_doc 			= form_persona.cleaned_data['nro_doc']
			persona.fecha_nac 			= form_persona.cleaned_data['fecha_nac']
			persona.sexo_id 			= form_persona.cleaned_data['sexo_id']
			persona.ciudad_nac 			= form_persona.cleaned_data['ciudad_nac']
			persona.pais_nac			= persona.ciudad_nac.pais
			persona.ciudad_res 			= form_persona.cleaned_data['ciudad_res']
			persona.estado_civil 		= form_persona.cleaned_data['estado_civil']

			personal.legajo 			= form.cleaned_data['legajo']
			personal.fecha_ingreso		= form.cleaned_data['fecha_ingreso']
			personal.ant_otro_organismo	= form.cleaned_data['ant_otro_organismo']
			personal.escalafon			= form.cleaned_data['escalafon']
			personal.credencial			= 0

			try:
				print persona
				persona.save()
				personal.save()
				form 			= PersonalForm()
				form_persona 	= PersonasForm()
				persona 		= Personas()
				personal 		= Personal()
			except Exception, e:
				raise e

	lista 			= Personal.objects.filter(borrado=False)
	return render_to_response('personal/abm.html',{'form':form,'personal':personal,'form_persona':form_persona,'persona':persona,'lista':lista},context_instance=RequestContext(request))	
	 
def remove_personal(request,id):
	personal = Personal.objects.get(id=id)
	personal.borrado = True
	personal.save()

	return HttpResponseRedirect(reverse('alta_personal'))