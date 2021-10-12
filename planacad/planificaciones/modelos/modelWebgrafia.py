from django.db import models

from planificaciones.modelos.modelPlanificacion import Planificacion

class Webgrafia(models.Model): 
   autor = models.CharField(max_length=200)
   titulo_publicacion = models.CharField(max_length=100)
   nombre_pagina = models.CharField(max_length=100)
   fecha_publicacion = models.DateField()
   link_pagina = models.CharField(max_length=100)
   es_obligatorio =  models.BooleanField(default=True)

   # Relations
   planificacion = models.ForeignKey(Planificacion, on_delete=models.CASCADE, null=True)

   def __str__(self):
        return "%s, %s" %(self.autor,self.titulo_publicacion)
