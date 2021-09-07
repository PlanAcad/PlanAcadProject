from planificaciones.modelos.modelPlanificacion import Planificacion


from planificaciones.modelos.modelPlanificacion import Planificacion
from django.db import models


class Unidad(models.Model): 
   id = models.AutoField(primary_key=True) 
   nombre_unidad = models.CharField(max_length=50)
   planificiacion = models.ForeignKey(Planificacion, on_delete=models.CASCADE, null=True, blank=True)
   def __str__(self):
        return "%s, %s" % (self.nombre_unidad,self.contenido)