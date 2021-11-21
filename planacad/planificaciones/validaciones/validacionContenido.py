from planificaciones.modelos.modelContenido import Contenido
from planificaciones.modelos.modelUnidad import Unidad
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
        contenidos = None
        try:
            contenidos = Contenido.objects.filter(planificacion_id=id_planificacion)
        except:
            validacion_ok=False
            validacion_bad=True
            errores.append("No existen contenidos")
        if(not contenidos):
            validacion_ok=False
            validacion_bad=True
            errores.append("No existen contenidos")
        else:
            for contenido in contenidos:
                if(contenido is not None):
                        if(not contenido.objetivos):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("objetivos en el contenido "+str(contenido.id))
                        if(not contenido.contenido):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("contenido en el contenido "+str(contenido.id))
                        if(not contenido.carga_horaria):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("carga_horaria en el contenido "+str(contenido.id))
                        if contenido.unidad is not None:
                            if(not contenido.unidad.numero):
                                validacion_ok=False
                                validacion_bad=True
                                errores.append("numero en la unidad"+str(contenido.unidad.id)+"en el contenido "+str(contenido.id))  
                            if(not contenido.unidad.titulo):
                                validacion_ok=False
                                validacion_bad=True
                                errores.append("titulo en la unidad"+str(contenido.unidad.id)+"en el contenido "+str(contenido.id))
                            if(not contenido.unidad.descripcion):
                                validacion_ok=False
                                validacion_bad=True
                                errores.append("descripcion en la unidad"+str(contenido.unidad.id)+"en el contenido "+str(contenido.id))
                             
    return [validacion_ok,validacion_bad,errores]