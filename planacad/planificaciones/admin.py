from django.contrib import admin

from .modelos.modelAsignatura import Asignatura
from .modelos.modelCarrera import Carrera
from .modelos.modelPlanificacion import Planificacion
from .modelos.modelProfesor import Profesor
from .modelos.modelDatosDescriptivos import DatosDescriptivos
from .modelos.modelFundamentacion import Fundamentacion
from .modelos.modelLibro import Libro
from .modelos.modelLibroWeb import LibroWeb




# Register your models here.
admin.site.register(Asignatura)
admin.site.register(Carrera)
admin.site.register(Planificacion)
admin.site.register(Profesor)
admin.site.register(DatosDescriptivos)
admin.site.register(Fundamentacion)
admin.site.register(Libro)
admin.site.register(LibroWeb)


