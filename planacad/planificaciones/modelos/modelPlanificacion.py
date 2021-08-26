from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelDatosDescriptivos import DatosDescriptivos

from django.db import models

class Planificacion(models.Model): 
   id = models.AutoField(primary_key=True) 
   fecha_Creacion = models.DateTimeField(max_length=50, auto_now=True)
   asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
   seccion1 = models.ForeignKey(DatosDescriptivos, on_delete=models.CASCADE, null=True, blank=True)

   def __str__(self):
        return "%s, %s" % (self.asignatura, self.fecha_Creacion)
   