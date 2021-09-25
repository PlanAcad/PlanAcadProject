# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  

from planificaciones.modelos.modelPlanificacion import Planificacion

def Bibliografia(request, id_planificacion):   
    planificacion = Planificacion.objects.get(id=id_planificacion)

    context = {
        'planificacion': planificacion,
    }

    return render(request,"secciones/bibliografia/index.html", context) 