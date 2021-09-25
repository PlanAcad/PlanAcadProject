
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelCondicion import CondicionAprobacionDirecta, CondicionAprobacionCursada
from planificaciones.formularios.formCondicion import  CondicionAprobacionDirectaForm, CondicionAprobacionCursadaForm

def AprobacionDirecta(request, id_planificacion):  
    planificacion = Planificacion.objects.get(id=id_planificacion)
    condicion_aprobacion_directa = CondicionAprobacionDirecta.objects.get(id=planificacion.condicion_aprobacion_directa.id)
    form = CondicionAprobacionDirectaForm(instance = condicion_aprobacion_directa)
    mensaje_exito = None
    mensaje_error = None
    
    if request.method == 'POST':  
        form = CondicionAprobacionDirectaForm(request.POST,instance = condicion_aprobacion_directa)
        if form.is_valid():
            try:
                form.save()                            
                mensaje_exito = "Guardamos los cambios correctamente."
               
            except:
                mensaje_error = "No pudimos guardar los cambios."


    context = {
        'planificacion': planificacion,
        'condicion_aprobacion_directa': condicion_aprobacion_directa, 
        'form': form, 
        'mensaje_exito': mensaje_exito, 
        'mensaje_error': mensaje_error
    }

    return render(request, "secciones/condicion/aprobacion-directa.html", context)  



def AprobacionCursada(request, id_planificacion):  
    planificacion = Planificacion.objects.get(id=id_planificacion)
    condicion_aprobacion_cursada = CondicionAprobacionCursada.objects.get(id=planificacion.condicion_aprobacion_cursada.id)
    form = CondicionAprobacionCursadaForm(instance = condicion_aprobacion_cursada)
    mensaje_exito = None
    mensaje_error = None
    
    if request.method == 'POST':  
        form = CondicionAprobacionCursadaForm(request.POST,instance = condicion_aprobacion_cursada)
        if form.is_valid():
            try:
                form.save()                            
                mensaje_exito = "Guardamos los cambios correctamente."
               
            except:
                mensaje_error = "No pudimos guardar los cambios."


    context = {
        'planificacion': planificacion,
        'condicion_aprobacion_cursada': condicion_aprobacion_cursada, 
        'form': form, 
        'mensaje_exito': mensaje_exito, 
        'mensaje_error': mensaje_error
    }

    return render(request, "secciones/condicion/aprobacion-cursada.html", context)  


