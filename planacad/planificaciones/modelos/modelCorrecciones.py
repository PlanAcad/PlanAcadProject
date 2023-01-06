from django.db import models
from planificaciones.modelos.modelPlanificacion import Planificacion

ESTADO_CORRECCION = [
      ('G', 'Generado'),
      ('R', 'Resuelto')
]

class Correccion(models.Model):
    id = models.AutoField(primary_key=True) 
    correccion = models.CharField(max_length=500)
    seccion = models.IntegerField(default=1, blank=True, null=True)
    estado = models.CharField(max_length=15, blank=True, null=True, choices=ESTADO_CORRECCION)

    planificacion = models.ForeignKey(Planificacion, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
       return "%s" % (self.correccion)
