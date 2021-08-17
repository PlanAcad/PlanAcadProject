from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelCarrera import Carrera
from django.db import models

class Seccion1(models.Model): 
   id = models.AutoField(primary_key=True) 
   institucion = models.DateTimeField(max_length=50)
   departamento =models.DateTimeField(max_length=50)
   areaBloque = models.DateTimeField(max_length=50)
   porcentajeHorasenCarrera =models.DateTimeField(max_length=50)
   porcentajeHorasenArea = models.DateTimeField(max_length=50)
   nivel = models.DateTimeField(max_length=50)
   cicloLectivo = models.DateTimeField(max_length=50)
   cargaHorariaTotal = models.DateTimeField(max_length=50)
   cargaHorariaSemanal = models.DateTimeField(max_length=50)
   cursado = models.DateTimeField(max_length=50)
   
   carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE) 
   asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE) 