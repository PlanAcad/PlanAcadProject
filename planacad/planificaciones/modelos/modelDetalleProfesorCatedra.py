from django.db import models
from planificaciones.modelos.modelCategoria import Categoria
from planificaciones.modelos.modelDedicacion import Dedicacion
from planificaciones.modelos.modelSituacion import Situacion
from django.contrib.auth.models import User
from planificaciones.modelos.modelTareasFunciones import TareasFunciones
from planificaciones.modelos.modelPlanificacion import Planificacion

class DetalleProfesorCatedra(models.Model): 
   planificacion = models.ForeignKey(Planificacion,on_delete=models.CASCADE, null=True, blank=True)
   id = models.AutoField(primary_key=True)
   categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True) 
   situacion = models.ForeignKey(Situacion, on_delete=models.CASCADE, null=True, blank=True)
   dedicacion = models.ForeignKey(Dedicacion, on_delete=models.CASCADE, null=True, blank=True)  
   profesor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
   tareas = models.ManyToManyField(TareasFunciones, blank=True)
   
   actividades = models.CharField(max_length=3000, null=True, blank=True)
    
def __str__(self):
    return "%s, %s,%s,%s" % (self.categoria,self.dedicacion,self.situacion,self.profesor)