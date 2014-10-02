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
	lista 			= Personal.objects.all()
	return render_to_response('personal/abm.html',{'form':form,'personal':personal,'form_persona':form_persona,'persona':persona,'lista':lista},context_instance=RequestContext(request))