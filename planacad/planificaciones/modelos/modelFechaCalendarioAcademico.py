from django.db import models

ESTADO = [
    ('F', 'Feriado'),
    ('EF', 'Examen Final'),
    ('RI', 'Receso Invernal'),
    ('IF', 'Inicio/Fin Clase'),
    ('DN', 'Dia Normal')
    ]

class FechaCalendarioAcademico(models.Model):
    fecha = models.DateTimeField()
    nombre_mes = models.CharField(max_length=100,null=True)
    nombre_dia = models.CharField(max_length=100,null=True)
    descripcion = models.CharField(max_length=100,null=True)
    hay_clase = models.BooleanField(null=True)
    actividad = models.CharField( max_length=2, blank=True, null=True, choices=ESTADO)



    def __str__(self):
        return "%s, %s, %s" %(self.fecha,self.descripcion, self.actividad)