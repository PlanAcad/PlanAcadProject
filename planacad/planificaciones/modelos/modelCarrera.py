from django.db import models

class Carrera(models.Model): 
   id = models.AutoField(primary_key=True) 
   nombreCarrera = models.CharField(max_length=50)

   def __str__(self):
       return self.nombreCarrera