from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra
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
        if(not planificacion.numero_comisiones):
            validacion_ok=False
            validacion_bad=True
            errores.append("numero_comisiones")
        if(not planificacion.numero_estudiantes_comision):
            validacion_ok=False
            validacion_bad=True
            errores.append("numero_estudiantes_comision")

        detallesProfesoresCatedra = None
        try:
            detallesProfesoresCatedra = DetalleProfesorCatedra.objects.filter(planificacion_id=id_planificacion)
        except:
            validacion_ok=False
            validacion_bad=True
            errores.append("No existe ningun detalle de profesor")
        if(not detallesProfesoresCatedra):
            validacion_ok=False
            validacion_bad=True
            errores.append("No existe ningun detalle de profesor")
        else:
            for detalleProfesorCatedra in detallesProfesoresCatedra:
                if(detalleProfesorCatedra is not None):
                    
                    if(not detalleProfesorCatedra.actividades):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("actividades en el detalle "+str(detalleProfesorCatedra.id))
                    if(detalleProfesorCatedra.profesor is None):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("No hay profesor asignado al detalle "+str(detalleProfesorCatedra.id))
                    else:
                        if(not detalleProfesorCatedra.profesor.first_name):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("nombre en el profesor "+ str(detalleProfesorCatedra.profesor.id) +"en el detalle "+str(detalleProfesorCatedra.id))
                        if(not detalleProfesorCatedra.profesor.last_name):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("apellido en el profesor "+ str(detalleProfesorCatedra.profesor.id) +"en el detalle "+str(detalleProfesorCatedra.id))
                    if(detalleProfesorCatedra.categoria is None):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("No hay categoria asignado al detalle "+str(detalleProfesorCatedra.id))
                    else:
                        if(not detalleProfesorCatedra.categoria.categoria):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("categoria en la categoria "+ str(detalleProfesorCatedra.categoria.id) +"en el detalle "+str(detalleProfesorCatedra.id))
                    if(detalleProfesorCatedra.situacion is None):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("No hay una situacion asignada al detalle "+str(detalleProfesorCatedra.id))
                    else:
                        if(not detalleProfesorCatedra.situacion.situacion):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("situacion en la situacion "+ str(detalleProfesorCatedra.situacion.id) +"en el detalle "+str(detalleProfesorCatedra.id))
                    if(detalleProfesorCatedra.dedicacion is None):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("No hay una dedicacion asignada al detalle "+str(detalleProfesorCatedra.id))
                    else:
                        if(not detalleProfesorCatedra.dedicacion.dedicacion):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("dedicacion en la dedicacion "+ str(detalleProfesorCatedra.dedicacion.id) +"en el detalle "+str(detalleProfesorCatedra.id))
                            
    return [validacion_ok,validacion_bad,errores]