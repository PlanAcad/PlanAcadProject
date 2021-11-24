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
        if(not planificacion.justificacion_ordenanza):
            validacion_ok=False
            validacion_bad=True
            errores.append("justificacion_ordenanza")
    return [validacion_ok,validacion_bad,errores]