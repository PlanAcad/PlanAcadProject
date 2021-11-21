from planificaciones.modelos.modelPropuestaDesarrollo import PropuestaDesarrollo
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
        propuestasDeDesarrollo = None
        try:
            propuestasDeDesarrollo = PropuestaDesarrollo.objects.filter(planificacion_id=id_planificacion)
        except:
            validacion_ok=False
            validacion_bad=True
            errores.append("No existe ninguna clase")
        if(not propuestasDeDesarrollo):
            validacion_ok=False
            validacion_bad=True
            errores.append("No existe ninguna clase")
        else:
            for propuestaDeDesarrollo in propuestasDeDesarrollo:
                if(propuestaDeDesarrollo is not None):
                    if propuestaDeDesarrollo.subcompetencias.all() is not None:
                            for subcompetencia in propuestaDeDesarrollo.subcompetencias.all():
                                if subcompetencia is not None:
                                    if(not subcompetencia.descripcion):
                                        validacion_ok=False
                                        validacion_bad=True
                                        errores.append("descripcion en la subcompetencia"+str(subcompetencia.id)+"en la propuesta "+str(propuestaDeDesarrollo.id))
                    if propuestaDeDesarrollo.resultados_de_aprendizaje.all() is not None:
                            for resultadoDeAprendizaje in propuestaDeDesarrollo.resultados_de_aprendizaje.all():
                                if resultadoDeAprendizaje is not None:
                                    if(not resultadoDeAprendizaje.resultado):
                                        validacion_ok=False
                                        validacion_bad=True
                                        errores.append("resultado en el RA"+str(resultadoDeAprendizaje.id)+"en la propuesta "+str(propuestaDeDesarrollo.id))
                    if propuestaDeDesarrollo.unidades.all() is not None:
                            for unidad in propuestaDeDesarrollo.unidades.all():
                                if unidad is not None:
                                    if(not unidad.numero):
                                        validacion_ok=False
                                        validacion_bad=True
                                        errores.append("numero en la unidad"+str(unidad.id)+"en la propuesta "+str(propuestaDeDesarrollo.id))
                                    if(not unidad.titulo):
                                        validacion_ok=False
                                        validacion_bad=True
                                        errores.append("titulo en la unidad"+str(unidad.id)+"en la propuesta "+str(propuestaDeDesarrollo.id))
                                    if(not unidad.descripcion):
                                        validacion_ok=False
                                        validacion_bad=True
                                        errores.append("descripcion en la unidad"+str(unidad.id)+"en la propuesta "+str(propuestaDeDesarrollo.id))
                                    
                
                    if(not propuestaDeDesarrollo.actividad_dentro_aula):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("actividad_dentro_aula en la propuesta "+str(propuestaDeDesarrollo.id))
                    if(not propuestaDeDesarrollo.actividad_fuera_aula):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("actividad_fuera_aula en la propuesta "+str(propuestaDeDesarrollo.id))
                    if(not propuestaDeDesarrollo.tiempo_dentro_aula):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("tiempo_dentro_aula en la propuesta "+str(propuestaDeDesarrollo.id))
                    if(not propuestaDeDesarrollo.tiempo_fuera_aula):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("tiempo_fuera_aula en la propuesta "+str(propuestaDeDesarrollo.id))

                    if propuestaDeDesarrollo.bibliografias.all() is not None:
                            for bibliografia in propuestaDeDesarrollo.bibliografias.all():
                                if bibliografia is not None:
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
                    if propuestaDeDesarrollo.estrategias_ens.all() is not None:
                            for estrategiaDeEnseñanza in propuestaDeDesarrollo.estrategias_ens.all():
                                if estrategiaDeEnseñanza is not None:
                                    if(not estrategiaDeEnseñanza.key):
                                        validacion_ok=False
                                        validacion_bad=True
                                        errores.append("key en la estrategia de Enseñanza"+str(estrategiaDeEnseñanza.id)+"en la propuesta "+str(propuestaDeDesarrollo.id)) 
                                    if(not estrategiaDeEnseñanza.estrategia):
                                        validacion_ok=False
                                        validacion_bad=True
                                        errores.append("estrategia en la estrategia de Enseñanza"+str(estrategiaDeEnseñanza.id)+"en la propuesta "+str(propuestaDeDesarrollo.id))             
                    if(not propuestaDeDesarrollo.modo_agrupamiento):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("modo_agrupamiento en la propuesta "+str(propuestaDeDesarrollo.id))
                    if(not propuestaDeDesarrollo.materiales_equipamiento):
                        validacion_ok=False
                        validacion_bad=True
                        errores.append("materiales_equipamiento en la propuesta "+str(propuestaDeDesarrollo.id))
                   
                                    
                                   
                        
