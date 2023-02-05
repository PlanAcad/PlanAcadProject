# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
from django.urls import reverse

from django.http import HttpResponseRedirect
## import model and form
from planificaciones.formularios.formDetalleProfesorCatedra import DetalleProfesorCatedraForm
from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra
from planificaciones.modelos.modelTareasFunciones import TareasFunciones
from planificaciones.modelos.modelPlanificacion import Planificacion
#Agregar
from django.db.models import Q
from planificaciones.modelos.modelCorrecciones import Correccion
#Correcciones
from planificaciones.formularios.formCorreccion import CorreccionForm
#Comentarios
from planificaciones.formularios.formComentarios import ComentarioForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, Group 
from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelTareasFunciones import TareasFunciones



##Define request for Asignatura   
@login_required
def DetalleProfesorCatedraNew(request, id_planificacion):
    mensaje_exito=None
    mensaje_error=None
    
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = DetalleProfesorCatedra.objects.filter(planificacion = planificacion)
    #CORRECCIONES
    correcciones = Correccion.objects.filter(Q(planificacion_id = id_planificacion) & Q(seccion = 2)).prefetch_related('comentarios')
    existen_correcciones_pendientes = None
    #Forms Correcciones y Comentarios
    correccionForm = CorreccionForm()
    comentarioForm = ComentarioForm()
    
    for item in correcciones:
        print(item.estado)
        if(item.estado == "G"):
            existen_correcciones_pendientes = "Existen correcciones pendientes de resolver"

    if request.method == "POST":  
        form = DetalleProfesorCatedraForm(request.POST)  
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                #Guardo
                instance.save()
                form.save_m2m()                    
                mensaje_exito="Añadimos el docente correctamente."  
            except:  
                 mensaje_error = "No pudimos añadir el docente."    
    else:  
        form = DetalleProfesorCatedraForm()
        asignatura = Asignatura.objects.get(id= planificacion.asignatura.id)
        form.fields['profesor'].queryset = User.objects.filter(groups = Group.objects.get(name='profesor')).intersection(asignatura.profesor.all())
        form.fields['tareas'].queryset = TareasFunciones.objects.filter(planificacion_id = planificacion.id)
    #Agregar
    context = {
        'planificacion': planificacion,
        'data': data,
        'form':form,
        'correcciones':correcciones,
        #Forms Correcciones
        'correccion_form': correccionForm,
        'comentario_form':comentarioForm,
        #
        'existen_correcciones_pendientes':existen_correcciones_pendientes,
        'mensaje_exito': mensaje_exito, 
        'mensaje_error': mensaje_error
    }  
    return render(request,'secciones/detalles-profesor-catedra.html', context) 
  
@login_required
def DetalleProfesorCatedraUpdate(request, id_planificacion, id_detalleprofesorcatedra):  
    mensaje_exito = None
    mensaje_error = None
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = DetalleProfesorCatedra.objects.get(id=id_detalleprofesorcatedra)
    if request.method == "POST":  
        form = DetalleProfesorCatedraForm(request.POST, instance=data)  
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                #Guardo
                instance.save()
                form.save_m2m()
                mensaje_exito="Guardamos los cambios correctamente."
                return redirect('planificaciones:detallesprofesorcatedra', id_planificacion=id_planificacion)
                 
            except:  
                 mensaje_error = "No pudimos guardar los cambios."    
    else:  
        form = DetalleProfesorCatedraForm(instance=data)  
        asignatura = Asignatura.objects.get(id= planificacion.asignatura.id)
        form.fields['profesor'].queryset = User.objects.filter(groups = Group.objects.get(name='profesor')).intersection(asignatura.profesor.all())
        form.fields['tareas'].queryset = TareasFunciones.objects.filter(planificacion_id = planificacion.id)

    return render(request,'secciones/detalles-profesor-catedra-update.html',{'data':data,'planificacion':planificacion,'form':form, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 
  
    
@login_required
def DetalleProfesorCatedraDestroy(request, id_planificacion, id_detalleprofesorcatedra):
    mensaje_exito = None
    mensaje_error = None
    if request.method == "POST":
        try:
            detalleProfesorCatedra = DetalleProfesorCatedra.objects.get(id=id_detalleprofesorcatedra)  
            detalleProfesorCatedra.delete()
            mensaje_exito = "Se ha borrado correctamente."        
        except:
            mensaje_error = "No pudimos borrar correctamente"  
        
        return redirect('planificaciones:detallesprofesorcatedra', id_planificacion=id_planificacion)
                 