import datetime
from django.db import models
from django.contrib.auth.models import User
from planificaciones.modelos.modelContenido import Contenido
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelResultadoAprendizaje import ResultadoDeAprendizaje

TIPO_EXAMEN = [
      ('P', 'Examen parcial'),
      ('R', 'Examen recuperatorio'),
      ('F', 'Examen final'),
      ('NA', 'No aplica')
]

class Clase(models.Model): 
   planificacion =models.ForeignKey(Planificacion, on_delete=models.CASCADE, null=True)
   lugar_desarrollo_de_clase = models.CharField(max_length=400, blank=True, null=True)
   fecha_clase = models.DateField(blank=True, null=True, default=datetime.date.today())
   es_examen = models.CharField(max_length=50, blank=True, null=True, choices=TIPO_EXAMEN)
   numero_de_clase_o_semana = models.IntegerField(default=0, blank=True, null=True)
   cantidad_tareas = models.IntegerField(default=0, blank=True, null=True)
   
   unidad_tematica_o_tema = models.ManyToManyField(Contenido, blank=True, null=True)
   resultado_de_aprendizaje = models.ManyToManyField(ResultadoDeAprendizaje, blank=True, null=True)
   profesor_a_cargo = models.ManyToManyField(User, blank=True, null=True)

   def __str__(self):
        return "%s, %s" %(self.unidad_tematica_o_tema,self.fecha_clase)