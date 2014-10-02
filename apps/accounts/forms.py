#! /usr/bin/python
# -*- encoding: utf-8 -*-

from django import forms 
#from apps.epa.models import *
from django.forms import ModelForm, TimeField
from django.contrib import admin
from django.utils import timezone 
from django.conf import settings
from django.contrib.auth.models import  Group,Permission,User
from django.contrib.admin import widgets
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms.widgets import CheckboxSelectMultiple
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
	usuario = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'required span9','placeholder':'Usuario'})))
	password = forms.CharField(widget=forms.PasswordInput(attrs=dict({'class':'required span9','placeholder':'Contraseña'}), render_value=False))
