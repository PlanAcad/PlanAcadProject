from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelCarrera import Carrera
from django.db import models

class Seccion1(models.Model): 
    
   id = models.AutoField(primary_key=True) 
   institucion = models.CharField(max_length=50, null=True, blank=True)
   departamento =models.CharField(max_length=50, null=True, blank=True)
   areaBloque = models.CharField(max_length=50, null=True, blank=True)
   porcentajeHorasenCarrera =models.CharField(max_length=50, null=True, blank=True)
   porcentajeHorasenArea = models.CharField(max_length=50, null=True, blank=True)
   nivel = models.CharField(max_length=50, null=True, blank=True)
   cicloLectivo = models.IntegerField(null=True, blank=True)
   cargaHorariaTotal = models.FloatField(max_length=50, null=True, blank=True)
   cargaHorariaSemanal = models.FloatField(max_length=50, null=True, blank=True)
   cursadoPosible=[
    ('A','Anual'),
    ('1','1er Cuatrimestre'),
    ('2','2do Cuatrimestre')
    ]
   cursado = models.CharField(max_length=1, null=True, blank=True,choices=cursadoPosible, default="A")
   
   carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, null=True, blank=True) 
   asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, null=True, blank=True) 

   def __str__(self):
       return "%s, %s" % (self.carrera, self.asignatura)