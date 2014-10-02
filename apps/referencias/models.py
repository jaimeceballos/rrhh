#! /usr/bin/python
# -*- encoding: utf-8 -*-|

from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import Group,Permission,User
from django.db.models import signals

class RefPaises(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField("Seleccione Pais :", unique=True, max_length=45L )
    

    def __unicode__(self):
      return  u'%s' % (self.descripcion)  
      self.descripcion = self.descripcion.upper()
     
    
    class Meta: 
        ordering = ["descripcion"]
        db_table = 'ref_paises'

    def save(self, force_insert=False, force_update=False):
        self.descripcion = self.descripcion.upper()
        super(RefPaises, self).save(force_insert, force_update)        


class RefProvincia(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField("Ingrese Provincia :", max_length=45L)
    pais = models.ForeignKey(RefPaises,on_delete=models.PROTECT)
    

    def __unicode__(self):
        return  u'%s' % (self.descripcion)
        self.descripcion = self.descripcion.upper()

    
    def save(self, force_insert=False, force_update=False):
        self.descripcion = self.descripcion.upper()
        super(RefProvincia, self).save(force_insert, force_update)

    class Meta:
        unique_together=('descripcion','pais',)
        db_table = 'ref_provincia'
        ordering = ["descripcion"]
     
class RefDepartamentos(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField("Ingrese Departamento :", unique=True, max_length=45L)
    provincia = models.ForeignKey(RefProvincia, on_delete=models.PROTECT)
       
    def __unicode__(self):
        return  u'%s' %  (self.descripcion)
        self.descripcion = self.descripcion.upper()
        
    
    def save(self, force_insert=False, force_update=False):
        self.descripcion = self.descripcion.upper()
        super(RefDepartamentos, self).save(force_insert, force_update)

    class Meta:
        #unique_together=('descripcion','provincia',)
        ordering = ["descripcion"]
        db_table = 'ref_departamentos'
        
class RefCiudades(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=80L)
    departamento = models.ForeignKey('RefDepartamentos',blank=True, null=True, on_delete=models.PROTECT)
    provincia = models.ForeignKey('RefProvincia', blank=True,  null=True, on_delete=models.PROTECT)
    pais = models.ForeignKey('RefPaises', on_delete=models.PROTECT)
    
    def __unicode__(self):
        return  u'%s' %  (self.descripcion)
        self.descripcion = self.descripcion.upper()

    def save(self, force_insert=False, force_update=False):
        self.descripcion = self.descripcion.upper()
        super(RefCiudades, self).save(force_insert, force_update)

    class Meta:
        unique_together = ('pais','provincia','departamento','descripcion',)
        ordering = ["descripcion"]
        db_table = 'ref_ciudades'

class RefTipoJerarquia(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField(max_length = 45)
 
    def __unicode__(self):
        return u'%s' % (self.descripcion)
        self.descripcion = self.descripcion.upper()
 
    class Meta:
        ordering = ['descripcion']
        db_table = 'ref_tipo_jerarquia'
 
class RefDivisionJerarquia(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField(max_length = 45)
 
    def __unicode__(self):
        return u'%s' % (self.descripcion)
        self.descripcion = self.descripcion.upper()
 
    class Meta:
        ordering = ['descripcion']
        db_table = 'ref_division_jerarquia'
 
class RefJerarquias(models.Model):
    id = models.AutoField(primary_key = True)
    descripcion = models.CharField(max_length = 45)
    ref_tipo_jerarquia = models.ForeignKey('RefTipoJerarquia',on_delete = models.PROTECT)
    ref_division_jerarquia = models.ForeignKey('RefDivisionJerarquia', on_delete = models.PROTECT)
 
    def __unicode__(self):
        return u'%s' % (self.descripcion)
        self.descripcion = self.descripcion.upper()
 
    class Meta:
        ordering = ['descripcion']
        db_table = 'ref_jerarquias'

class RefSexo(models.Model):
    id = models.AutoField(primary_key = True)
    Sexo_opciones=(
    ('1','Femenino'),
    ('2','Masculino'),
    )
    descripcion = models.CharField(max_length = 10, choices=Sexo_opciones)

    def __unicode__(self):
        return u'%s' % (self.descripcion)
  
    class Meta:
        ordering = ['descripcion']
        db_table = 'ref_sexo'

class RefEstadosciv(models.Model):
    id = models.AutoField(primary_key = True)
    civil_opciones=(
    ('0','NO REGISTRA'),('1','SOLTERO'),('2','CONCUBINO'),('3','CASAD0'),('4','DIVORCIADO'),('5','VIUDO'),('6','SEPARADO'),)
    descripcion = models.CharField(max_length = 10, choices=civil_opciones)

    def __unicode__(self):
        return u'%s' % (self.descripcion)
  
    class Meta:
        ordering = ['descripcion']
        db_table = 'ref_estadociv'  

class RefTipoDocumento(models.Model):
    id = models.AutoField(primary_key = True)
    Doc_opciones=(
    ('1','DNI'),
    ('2','LC'),
    ('3','LE'),
    ('4','CI'),
    ('5','PAS'),
    ('6','NO POSEE'),
    )
    descripcion = models.CharField(max_length = 8, choices= Doc_opciones)

    def __unicode__(self):
        return u'%s' % (self.descripcion)
 
    class Meta:
        ordering = ['descripcion']
        db_table = 'ref_tipodocumento'


class UnidadesRegionales(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=80L)
    ciudad = models.ForeignKey('RefCiudades',on_delete=models.PROTECT)
     
    def __unicode__(self):
        return u'%s' %  (self.descripcion)
        self.descripcion = self.descripcion.upper()
         
 
    def save(self, force_insert=False, force_update=False):
        self.descripcion = self.descripcion.upper()
        super(UnidadesRegionales, self).save(force_insert, force_update)
 
    class Meta:
        unique_together = ('descripcion','ciudad')
        ordering = ["descripcion"]
        db_table = 'unidades_regionales'

class Dependencias(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=80)
    unidades_regionales = models.ForeignKey('UnidadesRegionales', related_name="unidades", on_delete=models.PROTECT)
    ciudad = models.ForeignKey('RefCiudades',on_delete=models.PROTECT)
   
 
    def __unicode__(self):
        return u'%s' % (self.descripcion)
        self.descripcion = self.descripcion.upper()
 
    def save(self, force_insert=False, force_update= False):
        self.descripcion = self.descripcion.upper()
        super(Dependencias, self).save(force_insert,force_update)
 
    class Meta:
        unique_together = ('descripcion','unidades_regionales','ciudad')
        ordering = ["descripcion"]
        db_table = 'dependencias'


class RefOcupacion(models.Model):
    id = models.AutoField(primary_key= True)
    descripcion = models.CharField(max_length=80,unique = True)

    def __unicode__(self):
        return u'%s' % (self.descripcion)
        self.descripcion = self.descripcion.upper()

    def save(self, force_insert=False,force_update=False):
        self.descripcion = self.descripcion.upper()
        super(RefOcupacion, self).save(force_insert,force_update)

    class Meta:
        ordering = ['descripcion']
        db_table = 'ref_ocupacion'


class RefLicencia(models.Model):
    codigo = models.CharField(max_length=5,unique=True)
    descripcion = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s - %s' % (self.codigo,self.descripcion)
        self.descripcion = self.descripcion.upper()
        self.codigo = self.codigo.upper()

    def save(self, force_insert=False,force_update=False):
        self.descripcion = self.descripcion.upper()
        self.codigo = self.codigo.upper()
        super(RefLicencia,self).save(force_insert,force_update)

    class Meta:
        ordering = ['codigo']
        db_table = 'ref_licencia'


class RefAgrupacion(models.Model):
    descripcion = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % (self.descripcion)
        self.descripcion = self.descripcion.upper()

    def save(self, force_insert=False,force_update=False):
        self.descripcion = self.descripcion.upper()
        super(RefAgrupacion,self).save(force_insert,force_update)

    class Meta:
        ordering = ['descripcion']
        db_table = 'ref_agrupacion'

class RefEscalafon(models.Model):
    agrupacion = models.ForeignKey('RefAgrupacion', related_name="agrupacion", on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % (self.descripcion)
        self.descripcion = self.descripcion.upper()

    def save(self, force_insert=False,force_update=False):
        self.descripcion = self.descripcion.upper()
        super(RefEscalafon,self).save(force_insert,force_update)

    class Meta:
        ordering = ['descripcion']
        db_table = 'ref_escalafon'