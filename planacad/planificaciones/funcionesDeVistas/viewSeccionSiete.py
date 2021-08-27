from django.http import HttpResponseRedirect
from django.shortcuts import render  
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelActividad import Actividad


def SeccionSieteView(request, planificacion_id): 
    planificacion = Planificacion.objects.get(id=planificacion_id)    
    actividades = Actividad.objects.filter(planificacion=planificacion)    

    context = {
        "planificacion": planificacion,
        "actividades": actividades,
    }

    return render(request,"secciones/seccion-ocho.html", context) 