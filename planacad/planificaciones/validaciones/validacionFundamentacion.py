from planificaciones.modelos.modelFundamentacion import Fundamentacion
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
        try:
            fundamentacion = Fundamentacion.objects.get(id=planificacion.fundamentacion_id)
        except:
            errores.append("No existe la seccion datos descriptivos")
        if(fundamentacion is not None):
                if(not fundamentacion.fundamentos):
                    validacion_ok=False
                    validacion_bad=True
                    errores.append("fundamentos")
    return [validacion_ok,validacion_bad,errores]