from django.db import models
from django.contrib.auth.models import User
from planificaciones.modelos.modelPlanificacion import Planificacion

class PlanificacionUsuario(models.Model):
    planificacion = models.ForeignKey(Planificacion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)