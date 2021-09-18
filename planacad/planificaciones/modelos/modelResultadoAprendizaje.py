from django.db import models

class ResultadoDeAprendizaje(models.Model):
    descripcion = models.CharField(max_length=100)


    def __str__(self):
       return "%s, %s" % (self.id, self.descripcion)
         

