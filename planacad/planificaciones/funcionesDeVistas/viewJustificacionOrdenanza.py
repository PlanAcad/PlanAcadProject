
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.formularios.formJustificacionOrdenanza import  JustificacionOrdenanzaForm


def JustificacionOrdenanza(request, id_planificacion):  
    planificacion = Planificacion.objects.get(id=id_planificacion)
    form = JustificacionOrdenanzaForm(instance=planificacion)
    mensaje_exito = None
    mensaje_error = None
    
    print(planificacion.justificacion_ordenanza)
    if request.method == 'POST':  
        form = JustificacionOrdenanzaForm(request.POST,instance = planificacion)
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

    return render(request, "secciones/justificacion-ordenanza/index.html", context)  





