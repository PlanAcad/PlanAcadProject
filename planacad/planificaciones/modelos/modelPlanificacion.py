from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelDatosDescriptivos import DatosDescriptivos
from planificaciones.modelos.modelFundamentacion import Fundamentacion
from django.db import models

class Planificacion(models.Model): 
   id = models.AutoField(primary_key=True)
   estado = models.CharField(
        max_length=2,
        choices=[('P', 'En proceso'),('A', 'Aprobada'),('R', 'En revision'),('C', 'A corregir')]) 
   fecha_creacion = models.DateTimeField(max_length=50, auto_now=True)
   fecha_modificacion = models.DateTimeField(auto_now=True)
   asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
   eliminada = models.BooleanField(default=False, null=True)
   datos_descriptivos = models.ForeignKey(DatosDescriptivos, on_delete=models.CASCADE, null=True, blank=True)
   fundamentacion = models.ForeignKey(Fundamentacion, on_delete=models.CASCADE, null=True, blank=True)
   condicion_aprobacion_directa = models.CharField(max_length=6000, null=True, blank=True)
   condicion_aprobacion_cursada = models.CharField(max_length=6000, null=True, blank=True)
   justificacion_ordenanza = models.CharField(max_length=3000, null=True, blank=True)
   numero_comisiones = models.IntegerField(null=True, blank=True, default=1)
   numero_estudiantes_comision = models.IntegerField(null=True, blank=True)
   sincronizado_calendario_academico = models.BooleanField(default=False, null=True)


   def __str__(self):
        return "%s, %s" % (self.asignatura,self.fecha_creacion)
   