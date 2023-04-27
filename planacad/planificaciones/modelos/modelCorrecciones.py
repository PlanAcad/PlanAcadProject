from django.db import models
from planificaciones.modelos.modelPlanificacion import Planificacion
from django.contrib.auth.models import User
import datetime


ESTADO_CORRECCION = [
      ('G', 'Generado'),
      ('R', 'Resuelto'),
      ('C', 'Cerrado')
      

]

class Correccion(models.Model):
    id = models.AutoField(primary_key=True) 
    correccion = models.CharField(max_length=300)
    seccion = models.IntegerField(default=1, blank=True, null=True)
    estado = models.CharField(max_length=15, blank=True, null=True, choices=ESTADO_CORRECCION)
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creador_correccion', null=True,blank=True)
    usuarioQueResolvio = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resolvio_correccion', null=True)
    fechaDeCreacion = models.DateField(blank=True, null=True, default=datetime.date.today())

    planificacion = models.ForeignKey(Planificacion, on_delete=models.CASCADE, null=True, blank=True)
    
    class Meta:
      ordering = ['estado']
      
    def __str__(self):
       return "%s" % (self.correccion)         
