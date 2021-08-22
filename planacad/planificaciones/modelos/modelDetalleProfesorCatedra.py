from django.db import models
from modelCategoria import Categoria
from modelDedicacion import Dedicacion
from modelSituacion import Situacion
from modelTareasFunciones import TareasFunciones

class DetalleProfesorCatedra(models.Model): 
   id = models.AutoField(primary_key=True)
   categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True) 
   dedicacion = models.ForeignKey(Dedicacion, on_delete=models.CASCADE, null=True, blank=True) 
   situacion = models.ForeignKey(Situacion, on_delete=models.CASCADE, null=True, blank=True) 
   situacion = models.ManyToManyField(TareasFunciones, on_delete=models.CASCADE, null=True, blank=True) 
    

def __str__(self):
    return "%s, %s,%s" % (self.categoria,self.dedicacion,self.situacion)