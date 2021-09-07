from django.db import models

class Competencia(models.Model): 
   id = models.AutoField(primary_key=True) 
   tipo_competencia = models.CharField(max_length=50)
   competencia = models.CharField(max_length=50)

   def __str__(self):
        return "%s, %s" % (self.tipo_competencia, self.competencia)