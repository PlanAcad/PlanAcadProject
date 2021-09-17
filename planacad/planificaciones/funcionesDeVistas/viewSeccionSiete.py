from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelActividad import Actividad
from planificaciones.formularios.formSeccionSiete import ActividadForm


def SeccionSieteView(request, planificacion_id): 
    planificacion = Planificacion.objects.get(id=planificacion_id)    
    actividades = Actividad.objects.filter(planificacion=planificacion)  

    context = {
        "planificacion": planificacion,
        "actividades": actividades,
    }

    return render(request,"secciones/seccion-siete.html", context) 


def NewSeccionSiete(request, planificacion_id):
    planificacion = Planificacion.objects.get(id=planificacion_id)    
    actividades = Actividad.objects.filter(planificacion=planificacion)    

    form = ActividadForm()
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        print(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False) 
            new_form.planificacion = planificacion 
            new_form.save() 
            form.save_m2m() 
           
            return redirect("/planificacion/%s/seccion-siete" % (planificacion_id))

        else:
            print('not valid')
            print(form.errors)

    context = {
        "planificacion": planificacion,
        "actividades": actividades,
        "form": form
    }

    return render(request, "secciones/crear-seccion-siete.html", context)


def UpdateSeccionSiete(request, planificacion_id, actividad_id):
    planificacion = Planificacion.objects.get(id=planificacion_id)    
    actividad = Actividad.objects.get(id=actividad_id)
    
    form = ActividadForm(instance=actividad) 
    if request.method == 'POST':
        form = ActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            print('valid')

            print(request.POST)
            new_form = form.save(commit=False) 
            new_form.planificacion = planificacion 
            new_form.save() 
            form.save_m2m() 
           
            return redirect("/planificacion/%s/seccion-siete" % (planificacion_id))

        else:
            print('not valid')
            print(form.errors)



    context = {
        "planificacion": planificacion,
        "form": form
    }
    return render(request, "secciones/crear-seccion-siete.html", context)


def DeleteSeccionSiete(request, planificacion_id, actividad_id):
    planificacion = Planificacion.objects.get(id=planificacion_id)    
    actividad = Actividad.objects.get(id=actividad_id)

    if request.method == "POST":
        actividad.delete()
        return redirect("/planificacion/%s/seccion-siete" % (planificacion_id))

    context = {
        "planificacion": planificacion,
        "actividad": actividad,
    }
    return render(request,"secciones/eliminar-seccion-siete.html", context) 







