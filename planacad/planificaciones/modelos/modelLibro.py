from django.db import models
from planificaciones.modelos.modelPlanificacion import Planificacion

class Libro(models.Model): 
   id = models.AutoField(primary_key=True) 
   autores = models.CharField(max_length=50)
   año_de_publicacion = models.CharField(max_length=50)
   capitulos = models.CharField(max_length=50)
   editores = models.CharField(max_length=50)
   titulo_libro = models.CharField(max_length=50)
   ubicacion = models.CharField(max_length=50)
   planificacion = models.ForeignKey(Planificacion, on_delete=models.CASCADE, null=True, blank=True)

   def __str__(self):
        return "%s, %s, %s" %(self.titulo_libro,self.capitulos,self.autores)