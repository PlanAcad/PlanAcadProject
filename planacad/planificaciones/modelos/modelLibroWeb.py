from django.db import models
from planificaciones.modelos.modelPlanificacion import Planificacion

class LibroWeb(models.Model): 
   id = models.AutoField(primary_key=True) 
   autores = models.CharField(max_length=50)
   fecha_de_publicacion = models.CharField(max_length=50)
   titulo = models.CharField(max_length=50)
   nombre_pagina = models.CharField(max_length=50)
   url = models.CharField(max_length=60)
   planificacion = models.ForeignKey(Planificacion, on_delete=models.CASCADE, null=True, blank=True)

   def __str__(self):
        return "%s, %s, %s" %(self.titulo,self.url,self.autores)