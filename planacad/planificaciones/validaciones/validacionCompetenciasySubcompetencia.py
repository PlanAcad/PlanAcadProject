from planificaciones.modelos.modelSubCompetencia import SubCompetencia, Competencia
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
        competencias = None
        try:
            competencias = Competencia.objects.filter(planificacion_id=id_planificacion)
        except:
            validacion_ok=False
            validacion_bad=True
            errores.append("No existe ninguna competencia")
        if(not competencias):
            validacion_ok=False
            validacion_bad=True
            errores.append("No existe ninguna competencia")
        else:
            for competencia in competencias:
                if(competencia is not None):
                        if(not competencia.tipo_competencia):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("tipo_competencia en la competencia"+str(competencia.id))
                        if(not competencia.descripcion):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("descripcion en la competencia"+str(competencia.id))

                        if competencia.subcompetencia_set.all() is not None:
                            for subcompetencia in competencia.subcompetencia_set.all():
                                if subcompetencia is not None:
                                    if(not subcompetencia.descripcion):
                                        validacion_ok=False
                                        validacion_bad=True
                                        errores.append("descripcion en la subcompetencia"+str(subcompetencia.id)+"en la competencia "+str(competencia.id))
                            
    return [validacion_ok,validacion_bad,errores]