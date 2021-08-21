from django.db import models

class Situacion(models.Model): 
   id = models.AutoField(primary_key=True) 
   situacion = models.CharField( null=True, blank=True)

   def __str__(self) -> str:
       return self.situacion