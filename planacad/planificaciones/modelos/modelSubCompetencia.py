from django.db import models
from planificaciones.modelos.modelCompetencia import Competencia


class SubCompetencia(models.Model): 
   id = models.AutoField(primary_key=True) 
   descripcion = models.CharField(max_length=300, default="test")
   competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE)

   def __str__(self):
      #   return "%s" % (self.descripcion)
        return "%s - %s" % (self.competencia.tipo_competencia, self.descripcion)
