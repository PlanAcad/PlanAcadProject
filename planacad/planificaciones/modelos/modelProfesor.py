from django.db import models

class Profesor(models.Model): 
   id = models.AutoField(primary_key=True) 
   nombre = models.CharField(max_length=50)
   apellido = models.CharField(max_length=50)
   situacion = models.CharField(max_length=50)
   dedicacion = models.CharField(max_length=50)

   def __str__(self):
        return "%s, %s" % (self.nombre,self.apellido)