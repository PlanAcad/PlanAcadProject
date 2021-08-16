from planacad.planificaciones.modelos.modelCarrera import Carrera
from planacad.planificaciones.modelos.modelProfesor import Profesor
from django.db import models
from planificaciones.modelos.modelCarrera import Carrera

class Asignatura(models.Model): 
   id = models.AutoField(primary_key=True) 
   nombreMateria = models.CharField(max_length=50)
   carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
