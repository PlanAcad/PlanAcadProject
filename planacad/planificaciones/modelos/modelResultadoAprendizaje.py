from planificaciones.modelos.modelActividad import Actividad
from django.db import models

class ResultadoDeAprendizaje(models.Model):
    descripcion = models.CharField(max_length=100)

    # Relations 
    actividad = models.ManyToManyField(Actividad)

    def __str__(self):
       return "%s, %s, %s" % (self.id, self.descripcion, self.actividad)
         

