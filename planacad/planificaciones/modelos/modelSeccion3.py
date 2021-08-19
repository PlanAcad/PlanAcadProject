from django.db import models

class Profesor(models.Model): 
   id = models.AutoField(primary_key=True) 
   Fundamentos = models.CharField(max_length=6000)

   def __str__(self):
        return self.apellido