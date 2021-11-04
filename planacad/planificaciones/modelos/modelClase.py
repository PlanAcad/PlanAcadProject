from django.db import models
from planificaciones.modelos.modelProfesor import Profesor
from planificaciones.modelos.modelContenido import Contenido
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelResultadoAprendizaje import ResultadoDeAprendizaje

class Clase(models.Model): 
   planificacion =models.ForeignKey(Planificacion, on_delete=models.CASCADE)
   profesor_a_cargo = models.ForeignKey(Profesor, on_delete=models.CASCADE)
   lugar_desarrollo_de_clase = models.CharField(max_length=400, blank=True, null=True)
   fecha_clase = models.DateTimeField(max_length=50, auto_now=True)
   numero_de_clase_o_semena = models.CharField(max_length=400, blank=True, null=True)
   unidad_tematica_o_tema = models.ForeignKey(Contenido, on_delete=models.CASCADE)
   resultado_de_aprendizaje = models.ForeignKey(ResultadoDeAprendizaje, on_delete=models.CASCADE)

   def __str__(self):
        return "%s, %s" %(self.unidad_tematica_o_tema,self.fecha_clase)