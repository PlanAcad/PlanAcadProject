from django.db import models

class Dedicacion(models.Model): 
   id = models.AutoField(primary_key=True) 
   dedicacion = models.CharField( null=True, blank=True)

   def __str__(self) -> str:
       return self.dedicacion