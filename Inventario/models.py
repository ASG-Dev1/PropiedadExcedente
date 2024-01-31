import uuid
from django.db import models

from datetime import datetime


#from Usuarios.models import Usuario
# Create your models here.


class Auto(models.Model):
    vin = models.CharField(primary_key=True,max_length=255,default='', blank = False, null = False)
    marca = models.CharField(max_length=255,default='', blank = False, null = False)
    modelo = models.CharField(max_length=255,default='', blank = False, null = False)
    year = models.CharField(max_length=255,default='', blank = False, null = False)
    tablilla = models.CharField(max_length=255,default='', blank = False, null = False)
    color = models.CharField(max_length=255,default='', blank = False, null = False)
    cantidad = models.CharField(max_length=255,default='', blank = False, null = False)
    condicion = models.CharField(max_length=255,default='', blank = False, null = False)
    localizacion = models.CharField(max_length=255,default='', blank = False, null = False)
    creado = models.DateTimeField(default=datetime.now )
    archivo = models.ImageField(upload_to='excedente', blank=False, null=False)
    # usuario = models.CharField(User,max_length=30,default='')

 

class Articulo(models.Model):
   
    articuloid = models.CharField(max_length=255,default=uuid.uuid4)
    nombrearticulo = models.CharField(max_length=255,default='', blank = False, null = False)
    descripcion = models.CharField(max_length=255,default='', blank = False, null = False)
    cantidad = models.CharField(max_length=255,default='', blank = False, null = False)
    condicion = models.CharField(max_length=255,default='', blank = False, null = False)
    localizacion = models.CharField(max_length=255,default='', blank = False, null = False)
    creado = models.DateTimeField(default=datetime.now )
    archivo = models.ImageField(upload_to='excedente', blank=False, null=False)
    # usuario = models.CharField(User,max_length=30,default='')