# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class usuario(models.Model):
    Sexo = (
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
    )
    id_usuario = models.AutoField(primary_key = True)
    Nombre = models.OneToOneField(User,related_name="name")
    Apellidos = models.CharField(max_length=30)
    Edad = models.IntegerField(blank=True, null=True)
    Sexo = models.CharField(max_length =30, choices = Sexo)
    Email = models.CharField(max_length = 50)

    #Metodoto para poner nombre que se crea
    def __str__(self):
        return self.Nombre.username

class publicacion(models.Model):
    id_comentario = models.AutoField(primary_key = True)
    nombre = models.ForeignKey(usuario)
    texto = models.TextField()
    def __str__(self):
        return  str(self.id_comentario)

class comentario(models.Model):
    id_respuesta = models.AutoField(primary_key = True)
    id_comentario = models.ForeignKey(publicacion)
    nombre = models.ForeignKey(usuario)
    texto = models.TextField()
    
    def __str__(self):
        return str(self.id_comentario)

