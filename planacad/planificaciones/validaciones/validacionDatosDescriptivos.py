from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelCarrera import Carrera
from planificaciones.modelos.modelDatosDescriptivos import DatosDescriptivos
from planificaciones.modelos.modelPlanificacion import Planificacion

def ValidarSeccion(id_planificacion):
    validacion_ok=False
    validacion_bad =False
    errores = []
    planificacion = Planificacion.objects.get(id=id_planificacion)
    ##
    validacion_ok=True
    try:
        planificacion = Planificacion.objects.get(id=id_planificacion)
    except:
        validacion_ok=False
        validacion_bad=True
        errores.append("No existe la planificacion")
    if(planificacion is not None):
        try:
            datosDescriptivos = DatosDescriptivos.objects.get(id=planificacion.datos_descriptivos_id)
        except:
            errores.append("No existe la seccion datos descriptivos")
        if(datosDescriptivos is not None):
                if(not datosDescriptivos.institucion):
                    validacion_ok=False
                    validacion_bad=True
                    errores.append("institucion")
                if(not datosDescriptivos.departamento):
                    validacion_ok=False
                    validacion_bad=True
                    errores.append("departamento")
                if(not datosDescriptivos.area_bloque):
                    validacion_ok=False
                    validacion_bad=True
                    errores.append("area_bloque")
                if(not datosDescriptivos.porcentaje_horas_en_carrera):
                    validacion_ok=False
                    validacion_bad=True
                    errores.append("porcentaje_horas_en_carrera")
                if(not datosDescriptivos.porcentaje_horas_en_area):
                    validacion_ok=False
                    validacion_bad=True
                    errores.append("porcentaje_horas_en_area")
                if(not datosDescriptivos.nivel):
                    validacion_ok=False
                    validacion_bad=True
                    errores.append("nivel")
                if(datosDescriptivos.ciclo_lectivo is None):
                    validacion_ok=False
                    validacion_bad=True
                    errores.append("ciclo_lectivo")
                if(datosDescriptivos.carga_horaria_total is None):
                    validacion_ok=False
                    validacion_bad=True
                    errores.append("carga_horaria_total")
                if(datosDescriptivos.carga_horaria_semanal is None):
                    validacion_ok=False
                    validacion_bad=True
                    errores.append("carga_horaria_semanal")
                if(not datosDescriptivos.cursado):
                    validacion_ok=False
                    validacion_bad=True
                    errores.append("cursado")
                
                if(not datosDescriptivos.carrera):
                    validacion_ok=False
                    validacion_bad=True
                    errores.append("No tiene asignado una carrera")
                if(not datosDescriptivos.asignatura):
                    validacion_ok=False
                    validacion_bad=True
                    errores.append("No tiene asignado una asignatura")
        
    return [validacion_ok,validacion_bad,errores]
    