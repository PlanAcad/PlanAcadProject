from planificaciones.modelos.modelWebgrafia import Webgrafia
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
        webgrafias = None
        try:
            webgrafias = Webgrafia.objects.filter(planificacion_id=id_planificacion)
        except:
            validacion_ok=False
            validacion_bad=True
            errores.append("No existe ninguna webgrafia")
        if(not webgrafias):
            validacion_ok=False
            validacion_bad=True
            errores.append("No existe ninguna webgrafia")
        else:
            for webgrafia in webgrafias:
                if(webgrafia is not None):
                        if(not webgrafia.autor):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("autor en la webgrafia "+str(webgrafia.id))
                        if(not webgrafia.titulo_publicacion):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("titulo_publicacion en la webgrafia "+str(webgrafia.id))
                        if(not webgrafia.nombre_pagina):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("nombre_pagina en la webgrafia "+str(webgrafia.id))  
                        if(not webgrafia.fecha_publicacion):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("fecha_publicacion en la webgrafia "+str(webgrafia.id))  
                        if(not webgrafia.link_pagina):
                            validacion_ok=False
                            validacion_bad=True
                            errores.append("link_pagina en la webgrafia "+str(webgrafia.id))     
    return [validacion_ok,validacion_bad,errores]