from planificaciones.modelos.modelCarrera import Carrera
from planificaciones.modelos.modelProfesor import Profesor
from django.db import models

class Asignatura(models.Model): 
   id = models.AutoField(primary_key=True) 
   nombreMateria = models.CharField(max_length=50)
   carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
   profesor = models.ManyToManyField(Profesor)   
