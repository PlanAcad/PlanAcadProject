from django.db import models

class Categoria(models.Model): 
   id = models.AutoField(primary_key=True) 
   cateogoria = models.CharField( null=True, blank=True)

   def __str__(self) -> str:
       return self.cateogoria