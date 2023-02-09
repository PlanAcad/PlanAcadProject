from planificaciones.modelos.modelCarrera import Carrera
from django.contrib.auth.models import User
from django.db import models

class Asignatura(models.Model): 
   id = models.AutoField(primary_key=True) 
   nombre_materia = models.CharField(max_length=50)
   carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
   profesor = models.ManyToManyField(User)
   ano = models.CharField(max_length=1, blank=True, null=True)
   comision = models.CharField(max_length=1, blank=True, null=True)


   def __str__(self):
        return self.nombre_materia  
