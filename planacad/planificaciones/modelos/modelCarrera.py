from django.db import models
from django.contrib.auth.models import User

class Carrera(models.Model): 
   id = models.AutoField(primary_key=True) 
   nombre_carrera = models.CharField(max_length=50)
   users = models.ManyToManyField(User, blank=True, null=True, related_name = 'carrera')

   def __str__(self):
       return self.nombre_carrera