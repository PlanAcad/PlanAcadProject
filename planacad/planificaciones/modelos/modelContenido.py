from django.db import models

from planificaciones.modelos.modelPlanificacion import Planificacion

class Contenido(models.Model): 
   numero_unidad = models.IntegerField()
   titulo_unidad = models.CharField(max_length=100)
   objetivos = models.CharField(max_length=3000)
   contenido = models.CharField(max_length=5000)
   carga_horaria = models.CharField(max_length=100)

   # Relations
   planificacion = models.ForeignKey(Planificacion, on_delete=models.CASCADE, null=True)

   def __str__(self):
        return "%s, %s" %(self.numero_unidad,self.titulo_unidad)
