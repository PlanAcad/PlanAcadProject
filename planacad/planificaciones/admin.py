from django.contrib import admin

from .modelos.modelAsignatura import Asignatura
from .modelos.modelCarrera import Carrera
from .modelos.modelPlanificacion import Planificacion
from .modelos.modelProfesor import Profesor
from .modelos.modelDatosDescriptivos import DatosDescriptivos
from .modelos.modelFundamentacion import Fundamentacion
from .modelos.modelTipoDeEvaluacion import TipoDeEvaluacion
from .modelos.modelActividad import Actividad
from .modelos.modelResultadoAprendizaje import ResultadoDeAprendizaje
from .modelos.modelResultadoDeAprendizajeAnterior import ResultadoDeAprendizajeAnterior
from .modelos.modelCategoria import Categoria
from .modelos.modelDedicacion import Dedicacion
from .modelos.modelSituacion import Situacion
from .modelos.modelTareasFunciones import TareasFunciones
from .modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra
from .modelos.modelBibliografia import Bibliografia
from .modelos.modelWebgrafia import Webgrafia
from .modelos.modelContenido import Contenido





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
admin.site.register(DatosDescriptivos)
admin.site.register(Fundamentacion)
admin.site.register(TipoDeEvaluacion)
admin.site.register(Actividad)
admin.site.register(ResultadoDeAprendizaje)
admin.site.register(ResultadoDeAprendizajeAnterior)
admin.site.register(Bibliografia)
admin.site.register(Webgrafia)
admin.site.register(Contenido)





