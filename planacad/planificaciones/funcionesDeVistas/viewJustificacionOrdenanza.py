
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.formularios.formJustificacionOrdenanza import  JustificacionOrdenanzaForm
#Agregar
from django.db.models import Q
from planificaciones.modelos.modelCorrecciones import Correccion
#Correcciones
from planificaciones.formularios.formCorreccion import CorreccionForm
from planificaciones.funcionesDeVistas import viewCorreccion
#Comentarios
from planificaciones.formularios.formComentarios import ComentarioForm
from django.contrib.auth.decorators import login_required

@login_required
def JustificacionOrdenanza(request, id_planificacion):  
    planificacion = Planificacion.objects.get(id=id_planificacion)
    form = JustificacionOrdenanzaForm(instance=planificacion)
    mensaje_exito = None
    mensaje_error = None
    #CORRECCIONES
    correcciones = Correccion.objects.filter(Q(planificacion_id = id_planificacion) & Q(seccion = 13)).prefetch_related('comentarios')
    correcciones = viewCorreccion.OrderCorrecciones(correcciones)
    correccionesEnSecciones = viewCorreccion.CorreccionesEnSecciones(id_planificacion)
    existen_correcciones_pendientes = None
    #Forms Correcciones y Comentarios
    correccionForm = CorreccionForm()
    comentarioForm = ComentarioForm()
    
    for item in correcciones:
        print(item.estado)
        if(item.estado == "G"):
            existen_correcciones_pendientes = "Existen observaciones pendientes de resolver"
            
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
        'correcciones':correcciones,
        #Forms Correcciones
        'correccion_form': correccionForm,
        'comentario_form':comentarioForm,
        'correccionesEnSecciones':correccionesEnSecciones,
        #
        'existen_correcciones_pendientes':existen_correcciones_pendientes, 
        'mensaje_exito': mensaje_exito, 
        'mensaje_error': mensaje_error
    }

    return render(request, "secciones/justificacion-ordenanza/index.html", context)  





