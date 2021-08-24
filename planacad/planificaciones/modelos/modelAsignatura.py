from planificaciones.modelos.modelCarrera import Carrera
from django.db import models

class Asignatura(models.Model): 
   id = models.AutoField(primary_key=True) 
   nombreMateria = models.CharField(max_length=50)
   carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
   

   def __str__(self):
        return self.nombreMateria  
