from planificaciones.modelos.modelBibliografia import Bibliografia
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
        bibliografias = None
        try:
            bibliografias = Bibliografia.objects.filter(planificacion_id=id_planificacion)
        except:
            validacion_ok=False
            validacion_bad=True
            errores.append("No existe ninguna bibliografia")
        if(not bibliografias):
            validacion_ok=False
            validacion_bad=True
            errores.append("No existe ninguna bibliografia")
        else:
            for bibliografia in bibliografias:
                if(bibliografia is not None):
                        if(not bibliografia.autor):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("autor en la bibliografia "+str(bibliografia.id))
                        if(not bibliografia.titulo_libro):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("titulo_libro en la bibliografia "+str(bibliografia.id))
                        if(not bibliografia.editor):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("editor en la bibliografia "+str(bibliografia.id))  
                        if(not bibliografia.editor):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("año_publicacion en la bibliografia "+str(bibliografia.id))  
                        if(not bibliografia.editor):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("año_publicacion en la bibliografia "+str(bibliografia.id))
                        if(not bibliografia.nombre_capitulo):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("nombre_capitulo en la bibliografia "+str(bibliografia.id))
                        if(not bibliografia.ubicacion):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("ubicacion en la bibliografia "+str(bibliografia.id))        
    return [validacion_ok,validacion_bad,errores]