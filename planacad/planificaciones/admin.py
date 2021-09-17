from django.contrib import admin

from .modelos.modelAsignatura import Asignatura
from .modelos.modelCarrera import Carrera
from .modelos.modelPlanificacion import Planificacion
from .modelos.modelProfesor import Profesor
from planificaciones.modelos.modelDatosDescriptivos import DatosDescriptivos
from planificaciones.modelos.modelFundamentacion import Fundamentacion
from .modelos.modelTipoDeEvaluacion import TipoDeEvaluacion
from .modelos.modelActividad import Actividad
from .modelos.modelResultadoAprendizaje import ResultadoDeAprendizaje


# Register your models here.
admin.site.register(Asignatura)
admin.site.register(Carrera)
admin.site.register(Planificacion)
admin.site.register(Profesor)
admin.site.register(DatosDescriptivos)
admin.site.register(Fundamentacion)
admin.site.register(TipoDeEvaluacion)
admin.site.register(Actividad)
admin.site.register(ResultadoDeAprendizaje)


