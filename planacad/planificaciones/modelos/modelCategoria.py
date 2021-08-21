from django.db import models

class Categoria(models.Model): 
   id = models.AutoField(primary_key=True) 
   categoria = models.CharField( null=True, blank=True)

   def __str__(self) -> str:
       return self.categoria