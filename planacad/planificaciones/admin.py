from django.contrib import admin

from .modelos.modelAsignatura import Asignatura
from .modelos.modelCarrera import Carrera
from .modelos.modelPlanificacion import Planificacion
from .modelos.modelProfesor import Profesor
from .modelos.modelSeccion1 import Seccion1
from .modelos.modelTipoDeEvaluacion import TipoDeEvaluacion
from .modelos.modelActividad import Actividad
from .modelos.modelResultadoAprendizaje import ResultadoDeAprendizaje

# Register your models here.
admin.site.register(Asignatura)
admin.site.register(Carrera)
admin.site.register(Planificacion)
admin.site.register(Profesor)
admin.site.register(Seccion1)
admin.site.register(TipoDeEvaluacion)
admin.site.register(Actividad)
admin.site.register(ResultadoDeAprendizaje)
