from planificaciones.modelos.modelCompetencia import Competencia
from django.db import models


class SubCompetencia(models.Model): 
   id = models.AutoField(primary_key=True) 
   capacidad = models.CharField(max_length=50)
   competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE)

   def __str__(self):
        return "%s" % (self.capacidad)