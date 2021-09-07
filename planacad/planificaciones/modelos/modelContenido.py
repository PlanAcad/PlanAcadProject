from planificaciones.modelos.modelUnidad import Unidad
from django.db import models

class Contenido(models.Model): 
   id = models.AutoField(primary_key=True) 
   nombre_contenido = models.CharField(max_length=50)
   unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE, null=True, blank=True)
   def __str__(self):
        return "%s" % (self.nombre_contenido)