from planificaciones.modelos.modelAsignatura import Asignatura
from django.db import models

class Planificacion(models.Model): 
   id = models.AutoField(primary_key=True) 
   fechaCreacion = models.DateTimeField(max_length=50)
   asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)   