from django.db import models
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelPlanificacion import Planificacion

class ResultadoDeAprendizaje(models.Model):
    id = models.AutoField(primary_key=True) 
    resultado = models.CharField(max_length=300)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, null=True, blank=True) 
    planificacion = models.ForeignKey(Planificacion, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
       return "%s, %s" % (self.id, self.resultado)
         

