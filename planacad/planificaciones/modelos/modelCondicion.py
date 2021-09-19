from django.db import models

class CondicionAprobacionDirecta(models.Model): 
   descripcion = models.CharField(max_length=6000)

   def __str__(self):
        return str(self.id)

class CondicionAprobacionCursada(models.Model): 
   descripcion = models.CharField(max_length=6000)

   def __str__(self):
        return str(self.id)