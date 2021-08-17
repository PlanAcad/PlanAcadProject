from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelSeccion1 import Seccion1

from django.db import models

class Planificacion(models.Model): 
   id = models.AutoField(primary_key=True) 
   fechaCreacion = models.DateTimeField(max_length=50)
   asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
   seccion1 = models.ForeignKey(Seccion1, on_delete=models.CASCADE)