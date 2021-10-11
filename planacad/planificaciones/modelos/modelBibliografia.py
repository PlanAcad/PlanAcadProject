from django.db import models

from planificaciones.modelos.modelPlanificacion import Planificacion

class Bibliografia(models.Model): 
   autor = models.CharField(max_length=200)
   titulo_libro = models.CharField(max_length=100)
   editor = models.CharField(max_length=200, null=True, default="")
   año_publicacion = models.CharField(max_length=5)
   nombre_capitulo = models.CharField(max_length=50, null=True, default="")
   ubicacion = models.CharField(max_length=50, null=True, default="")
   es_obligatorio =  models.BooleanField(default=True)

   # Relations
   planificacion = models.ForeignKey(Planificacion, on_delete=models.CASCADE, null=True)

   def __str__(self):
        return "%s, %s" %(self.autor,self.titulo_libro)
