from django.db import models

class Carrera(models.Model): 
   id = models.AutoField(primary_key=True) 
   nombre_Carrera = models.CharField(max_length=50)

   def __str__(self) -> str:
       return self.nombre_Carrera