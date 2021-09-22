from planificaciones.modelos.modelPlanificacion import Planificacion
from django.db import models

class Competencia(models.Model): 
   id = models.AutoField(primary_key=True) 
   tipo_competencia = models.CharField(
        max_length=50,
        choices=[('T', 'Tecnológicas'),('E', 'Específicas'),('S', 'Sociales, políticas y actitudinales')],)
   descripcion = models.CharField(max_length=400, blank=True, null=True)
   planificacion = models.ForeignKey(Planificacion, on_delete=models.CASCADE)

   def __str__(self):
        return "%s, %s" % (self.tipo_competencia, self.descripcion)