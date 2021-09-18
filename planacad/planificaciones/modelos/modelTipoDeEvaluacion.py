from planificaciones.modelos.modelPlanificacion import Planificacion
from django.db import models

class TipoDeEvaluacion(models.Model):
    tipo = models.CharField(
        max_length=2,
        choices=[('D', 'Diagnóstica'),('F', 'Formativa'),('S', 'Sumativa'),('SF', 'Sumativa Final')])
    
    def __str__(self):
       return "id: %s, tipo: %s" % (self.id, self.get_tipo_display())