from django.db import models
from planificaciones.modelos.modelCorrecciones import Correccion
from django.contrib.auth.models import User
import datetime


class Comentario(models.Model):
    id = models.AutoField(primary_key=True) 
    comentario = models.CharField(max_length=500)
    creador = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    fechaDeCreacion = models.DateField(blank=True, null=True, default=datetime.date.today())
    correccion = models.ForeignKey(Correccion, on_delete=models.CASCADE, null=True, blank=True,related_name='comentarios') 

    def __str__(self):
       return "%s" % (self.comentario)
