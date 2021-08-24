from django.db import models
from planificaciones.modelos.modelCategoria import Categoria
from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra


class TareasFunciones(models.Model): 
   id = models.AutoField(primary_key=True)
   tareaFunciones = models.CharField(max_length=50) 
   categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True) 
   detalleprofesorcatedra = models.ManyToManyField(DetalleProfesorCatedra)
   def __str__(self) -> str:
       return self.tareaFunciones