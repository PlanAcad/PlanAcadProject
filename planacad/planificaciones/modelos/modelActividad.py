# planacad/planificaciones/modelos/modelActividad.py
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelTipoDeEvaluacion import TipoDeEvaluacion
from django.db import models

class Actividad(models.Model):
    actividad = models.CharField(
        max_length=2,
        choices=[('A', 'Autoevaluación'),('C', 'Coevaluación'),('H', 'Heteroevaluación')])
    unidad_tematica = models.CharField(max_length=30)
    lugar = models.CharField(max_length=20)
    indicadores_de_logro = models.CharField(max_length=100)
    tecnicas_de_evaluacion = models.CharField(max_length=100)

     # Relations 
    planificacion = models.ForeignKey(Planificacion, on_delete=models.CASCADE)
    tipo_de_evaluacion = models.ForeignKey(TipoDeEvaluacion, on_delete=models.CASCADE)

    def __str__(self):
       return "id: %s, actividad: %s" % (self.id, self.get_actividad_display())

