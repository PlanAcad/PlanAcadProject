from django.db import models

class Asignatura(models.Model): 
   id = models.AutoField(primary_key=True) 
   nombreMateria = models.CharField(max_length=50)