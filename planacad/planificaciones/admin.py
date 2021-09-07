from django.contrib import admin

from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelCarrera import Carrera
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelProfesor import Profesor
from planificaciones.modelos.modelDatosDescriptivos import DatosDescriptivos
from planificaciones.modelos.modelFundamentacion import Fundamentacion
from planificaciones.modelos.modelUnidad import Unidad
from planificaciones.modelos.modelContenido import Contenido




# Register your models here.
admin.site.register(Asignatura)
admin.site.register(Carrera)
admin.site.register(Planificacion)
admin.site.register(Profesor)
admin.site.register(DatosDescriptivos)
admin.site.register(Fundamentacion)
admin.site.register(Unidad)
admin.site.register(Contenido)


