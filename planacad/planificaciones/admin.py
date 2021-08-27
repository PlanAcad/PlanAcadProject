from django.contrib import admin

from .modelos.modelAsignatura import Asignatura
from .modelos.modelCarrera import Carrera
from .modelos.modelPlanificacion import Planificacion
from .modelos.modelProfesor import Profesor
from .modelos.modelSeccion1 import Seccion1



# Register your models here.
admin.site.register(Asignatura)
admin.site.register(Carrera)
admin.site.register(Planificacion)
admin.site.register(Profesor)
admin.site.register(Seccion1)

