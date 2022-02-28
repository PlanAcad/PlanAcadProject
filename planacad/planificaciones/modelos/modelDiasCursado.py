from django.db import models

class DiasCursado(models.Model): 
    
   id = models.AutoField(primary_key=True) 
   dia = models.CharField(max_length=50, null=True, blank=True)
   def __str__(self):
       return self.dia
