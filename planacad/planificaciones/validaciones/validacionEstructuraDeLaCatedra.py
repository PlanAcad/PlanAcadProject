from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra
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
        detallesProfesorCatedra = None
        try:
            detallesProfesorCatedra = DetalleProfesorCatedra.objects.filter(planificacion_id=id_planificacion)
        except:
            validacion_ok=False
            validacion_bad=True
            errores.append("No existe ningun detalle de profesores")
        if(not detallesProfesorCatedra):
            validacion_ok=False
            validacion_bad=True
            errores.append("No existe ningun detalle de profesores")
        else:
            for detalleProfesorCatedra in detallesProfesorCatedra:
                if(detalleProfesorCatedra is not None):
                    if(not detalleProfesorCatedra.categoria):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("No existe ninguns categoria")
                    else:
                        if(not detalleProfesorCatedra.categoria.categoria):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("categoria en el detalle "+str(detalleProfesorCatedra.id))
                    
                    if(not detalleProfesorCatedra.situacion):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("No existe ninguns situacion")
                    else:
                        if(not detalleProfesorCatedra.situacion.situacion):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("situacion en el detalle "+str(detalleProfesorCatedra.id))
                    
                    if(not detalleProfesorCatedra.dedicacion):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("No existe ninguns dedicacion")
                    else:
                        if(not detalleProfesorCatedra.dedicacion.dedicacion):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("dedicacion en el detalle "+str(detalleProfesorCatedra.id))
                    
                    if(not detalleProfesorCatedra.profesor):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("No existe ningun profesor")
                    else:
                        if(not detalleProfesorCatedra.profesor.first_name):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("nombre en el detalle "+str(detalleProfesorCatedra.id))
                        if(not detalleProfesorCatedra.profesor.last_name):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("apellido en el detalle "+str(detalleProfesorCatedra.id))

                    if(not detalleProfesorCatedra.tareas.all()):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("No existe ninguna tarea funcion en el detalle " + str(detalleProfesorCatedra.id))
                    else:
                        for tareaFuncion in detalleProfesorCatedra.tareas.all():
                            if(not tareaFuncion.tarea_funcion):
                                validacion_ok=False
                                validacion_bad=True
                                errores.append("tarea_funcion en "+str(detalleProfesorCatedra.id))
                            if(not tareaFuncion.categoria):
                                validacion_ok=False
                                validacion_bad=True
                                errores.append("No existe ninguns categoria en la tarea "+str(tareaFuncion.id)+ "del detalle "+str(detalleProfesorCatedra.id) )
                            else:
                                if(not detalleProfesorCatedra.categoria.categoria):
                                    validacion_ok=False
                                    validacion_bad=True
                                    errores.append("categoria en la tarea "+str(tareaFuncion.id)+ "del detalle "+str(detalleProfesorCatedra.id))

                            
                    
                                
    return [validacion_ok,validacion_bad,errores]