from django.db import models

class Dedicacion(models.Model): 
   id = models.AutoField(primary_key=True) 
   dedicacion = models.CharField(max_length=50)

   def __str__(self) -> str:
       return self.dedicacion