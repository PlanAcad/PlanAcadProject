from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelActividad import Actividad
from planificaciones.formularios.formSistemaDeEvaluacion import ActividadForm
#Agregar
from django.db.models import Q
from planificaciones.modelos.modelCorrecciones import Correccion
from planificaciones.formularios.formCorreccion import CorreccionForm


def SistemaDeEvaluacion(request, planificacion_id): 
    planificacion = Planificacion.objects.get(id=planificacion_id)    
    actividades = Actividad.objects.filter(planificacion=planificacion)
    #CORRECCIONES
    correcciones = Correccion.objects.filter(Q(planificacion_id = planificacion_id) & Q(seccion = 7)).prefetch_related('comentarios')
    existen_correcciones_pendientes = None
    correccion = CorreccionForm()
    for item in correcciones:
        print(item.estado)
        if(item.estado == "G"):
            existen_correcciones_pendientes = "Existen correcciones pendientes de resolver"

    form = ActividadForm()
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False) 
            new_form.planificacion = planificacion 
            new_form.save() 
            form.save_m2m() 
           
            return redirect('planificaciones:sistemaDeEvaluacion', planificacion_id=planificacion_id)

        else:
            print('not valid')
            print(form.errors)

    context = {
        "planificacion": planificacion,
        "actividades": actividades,
        "form": form,
        'correcciones':correcciones,
        'correccion_form': correccion,
        'existen_correcciones_pendientes':existen_correcciones_pendientes
    }

    return render(request,"secciones/sistema-de-evaluacion/index.html", context) 


def UpdateActividad(request, planificacion_id, actividad_id):
    planificacion = Planificacion.objects.get(id=planificacion_id)    
    actividad = Actividad.objects.get(id=actividad_id)
    
    form = ActividadForm(instance=actividad) 
    if request.method == 'POST':
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            new_form = form.save(commit=False) 
            new_form.planificacion = planificacion 
            new_form.save() 
            form.save_m2m() 
           
            return redirect('planificaciones:sistemaDeEvaluacion', planificacion_id=planificacion_id)


        else:
            print('not valid')
            print(form.errors)



    context = {
        "planificacion": planificacion,
        "form": form,
        "actividad": actividad,
    }
    return render(request, "secciones/sistema-de-evaluacion/update-actividad.html", context)


def DeleteActividad(request, planificacion_id, actividad_id):
    planificacion = Planificacion.objects.get(id=planificacion_id)    
    actividad = Actividad.objects.get(id=actividad_id)

    if request.method == "POST":
        actividad.delete()

        return redirect('planificaciones:sistemaDeEvaluacion', planificacion_id=planificacion_id)


    context = {
        "planificacion": planificacion,
        "actividad": actividad,
    }
    return render(request,"secciones/sistema-de-evaluacion/eliminar-actividad.html", context) 







