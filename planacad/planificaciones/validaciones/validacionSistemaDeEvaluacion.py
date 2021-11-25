from planificaciones.modelos.modelActividad import Actividad
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelTareasFunciones import TareasFunciones

def ValidarSeccion(id_planificacion):
    validacion_bad =False
    errores = []
    planificacion = Planificacion.objects.get(id=id_planificacion)
    validacion_ok=True
    try:
        planificacion = Planificacion.objects.get(id=id_planificacion)
    except:
        validacion_ok=False
        validacion_bad=True
        errores.append("No existe la planificacion")
    if(planificacion is not None):
        actividades = None
        try:
            actividades = Actividad.objects.filter(planificacion_id=id_planificacion)
        except:
            validacion_ok=False
            validacion_bad=True
            errores.append("No existe ninguna actividad")
        if(not actividades):
            validacion_ok=False
            validacion_bad=True
            errores.append("No existe ninguna actividad")
        else:
            for actividad in actividades:
                if(actividades is not None):
                    if(not actividad.actividad):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("actividad en la actividad "+str(actividad.id))
                    if(not actividad.unidad_tematica):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("unidad_tematica en la actividad "+str(actividad.id))
                    if(not actividad.lugar):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("lugar en la actividad "+str(actividad.id))
                    if(not actividad.indicadores_de_logro):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("indicadores_de_logro en la actividad "+str(actividad.id))
                    if(not actividad.tecnicas_de_evaluacion):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("tecnicas_de_evaluacion en la actividad "+str(actividad.id))
                   
                    if(actividad.tipo_de_evaluacion is None):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("No existe ningun tipo de evaluacion en la actividad "+str(actividad.id))
                    else:
                        if(not actividad.tipo_de_evaluacion.tipo):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("tipo en el tipo de evaluacion "+str(actividad.tipo_de_evaluacion.id)+"en la actividad "+str(actividad.id))
                    
                    if(not actividad.resultados_de_aprendizaje.all()):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("No existe ningun resultado de a´rendizaje en la actividad " + str(actividad.id))
                    else:
                        for resultadoDeAprendizaje in actividad.resultados_de_aprendizaje.all():
                            if(not resultadoDeAprendizaje.resultado):
                                validacion_ok=False
                                validacion_bad=True
                                errores.append("resultado en el resultado "+str(resultadoDeAprendizaje.id)+"en la actividad "+str(actividad.id))
                                
    return [validacion_ok,validacion_bad,errores]