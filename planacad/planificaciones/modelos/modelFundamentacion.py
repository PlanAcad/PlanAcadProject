from django.db import models

class Fundamentacion(models.Model): 
   id = models.AutoField(primary_key=True) 
   fundamentos = models.CharField(max_length=4000)

   def __str__(self):
        return str(self.id)