from planificaciones.modelos.modelClase import Clase
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
        clases = None
        try:
            clases = Clase.objects.filter(planificacion_id=id_planificacion)
        except:
            validacion_ok=False
            validacion_bad=True
            errores.append("No existe ninguna clase")
        if(not clases):
            validacion_ok=False
            validacion_bad=True
            errores.append("No existe ninguna clase")
        else:
            for clase in clases:
                if(clase is not None):
                    if clase.profesor_a_cargo.all() is not None:
                            for profesor in clase.profesor_a_cargo.all():
                                if profesor is not None:
                                    if(not profesor.first_name):
                                        validacion_ok=False
                                        validacion_bad=True
                                        errores.append("nombre en el profesor"+str(profesor.id)+"en la clase "+str(clase.id))
                                    if(not profesor.last_name):
                                        validacion_ok=False
                                        validacion_bad=True
                                        errores.append("apellido en el profesor"+str(profesor.id)+"en la clase "+str(clase.id))
                    if(not clase.lugar_desarrollo_de_clase):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("lugar_desarrollo_de_clase en la clase "+str(clase.id))
                    if(not clase.fecha_clase):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("fecha_clase en la clase "+str(clase.id))
                    if(not clase.es_examen):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("es_examen en la clase "+str(clase.id))
                    if(not clase.numero_de_clase_o_semana):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("numero_de_clase_o_semana en la clase "+str(clase.id))
                    if(not clase.cantidad_tareas):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("cantidad_tareas en la clase "+str(clase.id))
                    if clase.unidad_tematica_o_tema.all() is not None:
                            for unidadOTema in clase.unidad_tematica_o_tema.all():
                                if unidadOTema is not None:
                                    if(not unidadOTema.objetivos):
                                        validacion_ok=False
                                        validacion_bad=True
                                        errores.append("objetivos en la unidad o tema"+str(unidadOTema.id)+"en la clase "+str(clase.id))
                                    if(not unidadOTema.contenido):
                                        validacion_ok=False
                                        validacion_bad=True
                                        errores.append("contenido en la unidad o tema"+str(unidadOTema.id)+"en la clase "+str(clase.id))
                                    if(not unidadOTema.carga_horaria):
                                        validacion_ok=False
                                        validacion_bad=True
                                        errores.append("carga_horaria en la unidad o tema"+str(unidadOTema.id)+"en la clase "+str(clase.id))
                    if clase.resultado_de_aprendizaje.all() is not None:
                            for resultadoDeAprendizaje in clase.resultado_de_aprendizaje.all():
                                if resultadoDeAprendizaje is not None:
                                    if(not resultadoDeAprendizaje.resultado):
                                        validacion_ok=False
                                        validacion_bad=True
                                        errores.append("resultado en el resultado de aprendizaje"+str(resultadoDeAprendizaje.id)+"en la clase "+str(clase.id))
                                    
                                   
                        

                        
                            
    return [validacion_ok,validacion_bad,errores]