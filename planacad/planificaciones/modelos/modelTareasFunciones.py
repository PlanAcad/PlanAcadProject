from django.db import models
from modelCategoria import Categoria

class TareasFunciones(models.Model): 
   id = models.AutoField(primary_key=True)
   tareaFunciones = models.CharField(max_length=50) 
   categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True) 

   def __str__(self) -> str:
       return self.tareaFunciones