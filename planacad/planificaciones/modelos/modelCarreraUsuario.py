from planificaciones.modelos.modelCarrera import Carrera 
from django.contrib.auth.models import User
from django.db import models

class CarreraUsuario(models.Model): 
   id = models.AutoField(primary_key=True) 
   carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
   usuario = models.ForeignKey(User,on_delete=models.CASCADE)

   def __str__(self):
        return self.nombre_materia  
