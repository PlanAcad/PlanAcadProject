from django.contrib import admin

from .modelos.modelAsignatura import Asignatura
from .modelos.modelCarrera import Carrera
from .modelos.modelPlanificacion import Planificacion
from .modelos.modelProfesor import Profesor
from .modelos.modelCategoria import Categoria
from .modelos.modelDedicacion import Dedicacion
from .modelos.modelSituacion import Situacion
from .modelos.modelTareasFunciones import TareasFunciones
from .modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra
from .modelos.modelResultadoDeAprendizaje import ResultadoDeAprendizajes
from .modelos.modelDatosDescriptivos import DatosDescriptivos
from .modelos.modelFundamentacion import Fundamentacion

# Register your models here.
admin.site.register(Asignatura)
admin.site.register(Carrera)
admin.site.register(Planificacion)
admin.site.register(Profesor)
admin.site.register(Categoria)
admin.site.register(Dedicacion)
admin.site.register(Situacion)
admin.site.register(TareasFunciones)
admin.site.register(DetalleProfesorCatedra)
admin.site.register(ResultadoDeAprendizajes)
admin.site.register(DatosDescriptivos)
admin.site.register(Fundamentacion)

