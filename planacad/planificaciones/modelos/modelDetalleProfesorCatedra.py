from planificaciones.funcionesDeVistas.viewCarrera import profesor
from django.db import models
from planificaciones.modelos.modelCategoria import Categoria
from planificaciones.modelos.modelDedicacion import Dedicacion
from planificaciones.modelos.modelSituacion import Situacion
from planificaciones.modelos.modelProfesor import Profesor

class DetalleProfesorCatedra(models.Model): 
   id = models.AutoField(primary_key=True)
   categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True) 
   dedicacion = models.ForeignKey(Dedicacion, on_delete=models.CASCADE, null=True, blank=True) 
   situacion = models.ForeignKey(Situacion, on_delete=models.CASCADE, null=True, blank=True)
   profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=True, blank=True)
    
    

def __str__(self):
    return "%s, %s,%s,%s" % (self.categoria,self.dedicacion,self.situacion,self.profesor)