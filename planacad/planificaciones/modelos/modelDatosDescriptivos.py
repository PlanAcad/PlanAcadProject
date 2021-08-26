from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelCarrera import Carrera
from django.db import models

class DatosDescriptivos(models.Model): 
   id = models.AutoField(primary_key=True) 
   institucion = models.CharField(max_length=50, null=True, blank=True)
   departamento =models.CharField(max_length=50, null=True, blank=True)
   area_bloque = models.CharField(max_length=50, null=True, blank=True)
   porcentaje_horas_en_carrera =models.CharField(max_length=50, null=True, blank=True)
   porcentaje_horas_en_area = models.CharField(max_length=50, null=True, blank=True)
   nivel = models.CharField(max_length=50, null=True, blank=True)
   ciclo_lectivo = models.IntegerField( null=True, blank=True)
   carga_horaria_Total = models.FloatField(max_length=50, null=True, blank=True)
   carga_horaria_semanal = models.FloatField(max_length=50, null=True, blank=True)
   cursado = models.DateTimeField(max_length=50, null=True, blank=True)
   
   carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, null=True, blank=True) 
   asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, null=True, blank=True) 

   def __str__(self) -> str:
       return "%s, %s" % (self.carrera,self.asignatura)
       