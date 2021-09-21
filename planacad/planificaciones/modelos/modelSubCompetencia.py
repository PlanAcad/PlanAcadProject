from django.db import models


class SubCompetencia(models.Model): 
   id = models.AutoField(primary_key=True) 
   descripcion = models.CharField(max_length=300)

   def __str__(self):
        return "%s" % (self.capacidad)