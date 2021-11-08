from django.db import models

class Unidad(models.Model): 
   numero = models.IntegerField(blank=True, null=True)
   titulo = models.CharField(max_length=100)
   descripcion = models.CharField(max_length=1000)

   def __str__(self):
        return "%s, %s" %(self.numero,self.titulo)
