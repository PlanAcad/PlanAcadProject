from django.db import models

ESTADO = [
    ('IC1', 'Inicio de clases 1er cuatrimestre'),
    ('FC1', 'Fin de clases 1er cuatrimestre'),
    ('IC2', 'Inicio de clases 2do cuatrimestre'),
    ('FC2', 'Fin de clases 2do cuatrimestre'),
    ('EF', 'Examen final con suspensión de clase'),
    ('EF', 'Examen final sin suspensión de clase'),
    ('RI', 'Receso de invierno'),
    ('F', 'Feriado'),
    ('DN', 'Dia Normal')
    ]

class FechaCalendarioAcademico(models.Model):
    fecha = models.DateTimeField()
    nombre_mes = models.CharField(max_length=100,null=True)
    nombre_dia = models.CharField(max_length=100,null=True)
    descripcion = models.CharField(max_length=100,null=True)
    ciclo_lectivo = models.IntegerField(null=True)
    hay_clase = models.BooleanField(null=True)
    editable = models.BooleanField(null=True)
    actividad = models.CharField( max_length=4, blank=True, null=True, choices=ESTADO)



    def __str__(self):
        return "%s, %s, %s" %(self.fecha,self.descripcion, self.actividad)