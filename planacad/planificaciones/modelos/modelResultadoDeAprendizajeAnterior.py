from django.db import models
from planificaciones.modelos.modelResultadoAprendizaje import ResultadoDeAprendizaje
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelAsignatura import Asignatura


class ResultadoDeAprendizajeAnterior(models.Model):
    id = models.AutoField(primary_key=True)
    asignatura =models.ForeignKey(Asignatura, on_delete=models.CASCADE, null=True, blank=True) 
    resultado = models.ForeignKey(ResultadoDeAprendizaje, on_delete=models.CASCADE, null=True, blank=True)
    planificacion = models.ForeignKey(Planificacion, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
       return "%s, %s" % (self.id, self.resultado)
         

class ResultadoDeAprendizajeAnteriorPrimerNivel(models.Model):
    id = models.AutoField(primary_key=True)
    resultado = models.CharField(max_length=300)
    planificacion = models.ForeignKey(Planificacion, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
       return "%s, %s" % (self.id, self.resultado)
         
