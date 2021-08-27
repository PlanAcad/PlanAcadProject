from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelSeccion1 import Seccion1
from planificaciones.modelos.modelSeccion3 import Seccion3

from django.db import models

class Planificacion(models.Model): 
   id = models.AutoField(primary_key=True) 
   fechaCreacion = models.DateTimeField(max_length=50, auto_now=True)
   asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
   seccion1 = models.ForeignKey(Seccion1, on_delete=models.CASCADE, null=True, blank=True)
   seccion3 = models.ForeignKey(Seccion3, on_delete=models.CASCADE, null=True, blank=True)
   

   def __str__(self):
        return "%s, %s" % (self.asignatura,self.fechaCreacion)
   