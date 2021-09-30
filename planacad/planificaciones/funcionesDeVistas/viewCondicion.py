
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.formularios.formCondicion import  CondicionAprobacionDirectaForm, CondicionAprobacionCursadaForm

def AprobacionDirecta(request, id_planificacion):  
    planificacion = Planificacion.objects.get(id=id_planificacion)
    form = CondicionAprobacionDirectaForm(instance = planificacion)
    mensaje_exito = None
    mensaje_error = None
    
    if request.method == 'POST':  
        form = CondicionAprobacionDirectaForm(request.POST,instance = planificacion)
        if form.is_valid():
            try:
                form.save()                            
                mensaje_exito = "Guardamos los cambios correctamente."
               
            except:
                mensaje_error = "No pudimos guardar los cambios."


    context = {
        'planificacion': planificacion,
        'form': form, 
        'mensaje_exito': mensaje_exito, 
        'mensaje_error': mensaje_error
    }

    return render(request, "secciones/condicion/aprobacion-directa.html", context)  



def AprobacionCursada(request, id_planificacion):  
    planificacion = Planificacion.objects.get(id=id_planificacion)
    form = CondicionAprobacionCursadaForm(instance = planificacion)
    mensaje_exito = None
    mensaje_error = None
    
    if request.method == 'POST':  
        form = CondicionAprobacionCursadaForm(request.POST,instance = planificacion)
        if form.is_valid():
            try:
                form.save()                            
                mensaje_exito = "Guardamos los cambios correctamente."
               
            except:
                mensaje_error = "No pudimos guardar los cambios."


    context = {
        'planificacion': planificacion,
        'form': form, 
        'mensaje_exito': mensaje_exito, 
        'mensaje_error': mensaje_error
    }

    return render(request, "secciones/condicion/aprobacion-cursada.html", context)  


