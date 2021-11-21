from planificaciones.modelos.modelResultadoDeAprendizajeAnterior import ResultadoDeAprendizajeAnterior
from planificaciones.modelos.modelPlanificacion import Planificacion

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
        resultadosAnteriores = None
        try:
            resultadosAnteriores = ResultadoDeAprendizajeAnterior.objects.filter(planificacion_id=id_planificacion)
        except:
            validacion_ok=False
            validacion_bad=True
            errores.append("No existe ningun resultado de aprendizaje anterior")
        if(not resultadosAnteriores):
            validacion_ok=False
            validacion_bad=True
            errores.append("No existe ningun resultado de aprendizaje anterior")
        else:
            for resultadoAnterior in resultadosAnteriores:
                if(resultadoAnterior is not None):
                        if resultadoAnterior.asignatura is not None:
                            if(not resultadoAnterior.asignatura.nombre_materia):
                                validacion_ok=False
                                validacion_bad=True
                                errores.append("nombre_materia en asignatura"+str(resultadoAnterior.asignatura.id)+"en el resultado anterior "+str(resultadoAnterior.id))
                        
                        if resultadoAnterior.resultado is not None:
                            if(not resultadoAnterior.resultado.resultado):
                                validacion_ok=False
                                validacion_bad=True
                                errores.append("numero en el resultado"+str(resultadoAnterior.resultado.id)+"en el resultado anterior "+str(resultadoAnterior.id))  
                            
    return [validacion_ok,validacion_bad,errores]