from django.db import models
from planificaciones.modelos.modelPlanificacion import Planificacion

class Unidad(models.Model): 
   numero = models.IntegerField(blank=True, null=True)
   titulo = models.CharField(max_length=100)
   descripcion = models.CharField(max_length=1000)
   planificacion = models.ForeignKey(Planificacion, on_delete=models.CASCADE, null=True, blank=True)

   def __str__(self):
        return "%s- %s" %(self.numero,self.titulo)
