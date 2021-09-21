from django.db import models

class Situacion(models.Model): 
   id = models.AutoField(primary_key=True) 
   situacion = models.CharField(max_length=50)

   def __str__(self):
       return self.situacion