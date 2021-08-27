from django.db import models

class Seccion3(models.Model): 
   id = models.AutoField(primary_key=True) 
   fundamentos = models.CharField(max_length=6000)

   def __str__(self):
        return str(self.id)