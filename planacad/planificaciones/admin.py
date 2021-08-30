from django.contrib import admin

from .modelos.modelAsignatura import Asignatura
from .modelos.modelCarrera import Carrera
from .modelos.modelPlanificacion import Planificacion
from .modelos.modelProfesor import Profesor
from .modelos.modelSeccion1 import Seccion1
from .modelos.modelCategoria import Categoria
from .modelos.modelDedicacion import Dedicacion
from .modelos.modelSituacion import Situacion
from .modelos.modelTareasFunciones import TareasFunciones
from .modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra
from .modelos.modelResultadoDeAprendizaje import ResultadoDeAprendizaje


# Register your models here.
admin.site.register(Asignatura)
admin.site.register(Carrera)
admin.site.register(Planificacion)
admin.site.register(Profesor)
admin.site.register(Seccion1)
admin.site.register(Categoria)
admin.site.register(Dedicacion)
admin.site.register(Situacion)
admin.site.register(TareasFunciones)
admin.site.register(DetalleProfesorCatedra)
admin.site.register(ResultadoDeAprendizaje)



