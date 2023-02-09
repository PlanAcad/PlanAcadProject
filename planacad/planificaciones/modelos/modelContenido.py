from django.db import models

from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelUnidad import Unidad

class Contenido(models.Model): 
   objetivos = models.CharField(max_length=3000)
   contenido = models.CharField(max_length=5000)
   carga_horaria = models.CharField(max_length=100)

   # Relations
   planificacion = models.ForeignKey(Planificacion, on_delete=models.CASCADE, null=True)
   unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE, null=True)

   def __str__(self):
        return "%s, %s" %(self.unidad.numero, self.unidad.titulo)
