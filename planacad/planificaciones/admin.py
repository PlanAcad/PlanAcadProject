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
from .modelos.modelCompetencia import Competencia
from .modelos.modelSubCompetencia import SubCompetencia
from .modelos.modelPropuestaDesarrollo import PropuestaDesarrollo
from .modelos.modelPropuestaDesarrollo import EstrategiasEns
from .modelos.modelUnidad import Unidad
from .modelos.modelClase import Clase




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
admin.site.register(Competencia)
admin.site.register(SubCompetencia)
admin.site.register(PropuestaDesarrollo)
admin.site.register(EstrategiasEns)
admin.site.register(Unidad)
admin.site.register(Clase)




