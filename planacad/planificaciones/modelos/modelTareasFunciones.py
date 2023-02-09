from django.db import models
from planificaciones.modelos.modelCategoria import Categoria
from planificaciones.modelos.modelPlanificacion import Planificacion


class TareasFunciones(models.Model): 
   id = models.AutoField(primary_key=True)
   tarea_funcion = models.CharField(max_length=50) 
    # categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True) 
   planificacion = models.ForeignKey(Planificacion, on_delete=models.CASCADE, null=True, blank=True) 

   def __str__(self) -> str:
       return self.tarea_funcion