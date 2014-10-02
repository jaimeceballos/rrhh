# Create your views here.
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponseRedirect, HttpResponse, Http404
import datetime
from django.conf import settings
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from datetime import datetime
from django.forms.forms import NON_FIELD_ERRORS
from apps.accounts.forms import *
from django.views.decorators.cache import cache_control
from django.core import serializers

def login(request):
	form = LoginForm()
	error = ''
	if request.method =='POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			usuario = form.data['usuario']
			password = form.data['password']
			user = auth.authenticate(username=usuario,password=password)
			print user
			if user is not None and user.is_active:

				auth.login(request,user)
				return HttpResponseRedirect(reverse('home'))
			else:
				error = 'Usuario o clave incorrecto.'
				values={
					'form':form,
					'error':error,
				}
				return render_to_response('accounts/login.html',values, context_instance = RequestContext(request))
		else:
			error = 'Verifique los datos ingresados.'
			values={
				'form':form,
				'error':error,
			}
			return render_to_response('accounts/login.html',values, context_instance = RequestContext(request))
	values={
		'form':form,
	}
	return render_to_response('accounts/login.html',values, context_instance = RequestContext(request))


def logout(request):
	auth.logout(request)

	return HttpResponseRedirect(reverse('login'))