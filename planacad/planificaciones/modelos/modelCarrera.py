from django.db import models

class Carrera(models.Model): 
   id = models.AutoField(primary_key=True) 
   nombre_carrera = models.CharField(max_length=50)

   def __str__(self):
       return self.nombre_carrera