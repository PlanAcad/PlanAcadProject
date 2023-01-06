from django.db import models
from planificaciones.modelos.modelCorrecciones import Correccion


class Comentario(models.Model):
    id = models.AutoField(primary_key=True) 
    comentario = models.CharField(max_length=500)

    correccion = models.ForeignKey(Correccion, on_delete=models.CASCADE, null=True, blank=True,related_name='comentarios') 

    def __str__(self):
       return "%s" % (self.comentario)
