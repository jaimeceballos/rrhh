#! /usr/bin/python
# -*- encoding: utf-8 -*-|

from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import Group,Permission,User
from django.db.models import signals
from apps.referencias.models import *

class Personas(models.Model):
    id = models.AutoField(primary_key = True)
    apellidos = models.CharField(max_length = 100,verbose_name='apellidos')
    nombres = models.CharField(max_length = 150,verbose_name='nombres')
    tipo_doc = models.ForeignKey('referencias.RefTipoDocumento', verbose_name='tipo documento',on_delete = models.PROTECT)
    nro_doc = models.CharField(max_length=50)
    ciudad_nac = models.ForeignKey('referencias.RefCiudades',  blank = True, null = True,related_name='ciudad_nac', on_delete = models.PROTECT)
    pais_nac =models.ForeignKey('referencias.RefPaises',  blank = True, null = True,related_name='pais_nac', on_delete = models.PROTECT)
    ciudad_res = models.ForeignKey('referencias.RefCiudades', blank = True, null = True,related_name='ciudad_res', on_delete = models.PROTECT)
    sexo_id =  models.ForeignKey('referencias.RefSexo', on_delete = models.PROTECT)
    ocupacion = models.ForeignKey('referencias.RefOcupacion',blank = True, null = True,on_delete = models.PROTECT)
    cuit = models.CharField(max_length=11,default=0,blank = True, null = True)
    celular = models.CharField(max_length= 100,blank = True, null = True)
    fecha_nac = models.DateField()
    estado_civil=models.ForeignKey('referencias.RefEstadosciv',blank = True, null = True,on_delete = models.PROTECT)
    alias = models.CharField(max_length=150,blank = True, null = True)
    

    def __unicode__(self):
        return u'%s %s' % (self.apellidos, self.nombres)
        self.apellidos = self.descripcion.upper()
        self.nombres = self.nombres.upper()
 
    def save(self, force_insert = False, force_update = False):
        self.apellidos = self.apellidos.upper()
        self.nombres = self.nombres.upper()
        super(Personas, self).save(force_insert, force_update)    

    class Meta:
        unique_together=('tipo_doc','nro_doc','apellidos','nombres',)
        ordering = ['apellidos']
        db_table = 'personas'

class Personal(models.Model):
    id = models.AutoField(primary_key=True)
    persona_id = models.OneToOneField('Personas', unique=True,on_delete=models.PROTECT)
    legajo = models.CharField(max_length=6)
    credencial = models.IntegerField(blank=True,null=True)
    nro_cuenta_bco = models.CharField(max_length=20)
    nro_seros = models.CharField(max_length=15)
    fecha_ingreso = models.DateField(null=True,blank=True)
    ant_otro_organismo = models.IntegerField(null=True,blank=True)
    escalafon = models.ForeignKey('referencias.RefEscalafon',related_name='escalafon',on_delete=models.PROTECT)
    borrado = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s - %s, %s' % (self.persona_id.nro_doc,self.persona_id.apellidos,self.persona_id.nombres)
    
    class Meta:

        ordering = ['id']
        db_table = 'personal'