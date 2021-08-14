from django.db import models

# Create your models here.
class Asignatura(models.Model): 
   id = models.AutoField(primary_key=True) 
   nombreMateria = models.CharField(max_length=50)
