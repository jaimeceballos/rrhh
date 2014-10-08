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

def licencias(request):
	if request.method == 'POST':
		form = LicenciaForm(request.POST)
		if form.is_valid():
			form.save()
	form 	 = LicenciaForm()
	lista = Licencia.objects.all()
	return render_to_response('licencia/formulario_licencia.html',{'form':form,'lista':lista},context_instance=RequestContext(request))