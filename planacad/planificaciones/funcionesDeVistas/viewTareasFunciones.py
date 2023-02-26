# Para usar los objetos y/o funciones de 'redirect'
from planificaciones.modelos.modelCategoria import Categoria
from django.shortcuts import render, redirect 
from django.urls import reverse
## import model and form
from planificaciones.formularios.formTareasFunciones import TareasFuncionesForm
from planificaciones.modelos.modelTareasFunciones import TareasFunciones
from planificaciones.formularios.formDistribucionTareas import DistribucionTareasForm
from planificaciones.formularios.formDetalleProfesorCatedra import DetalleProfesorCatedraForm
from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra  
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelPlanificacion import Planificacion
from django.contrib.auth.decorators import login_required
from planificaciones.formularios.formContenido import ContenidoForm
from planificaciones.modelos.modelContenido import Contenido
#Agregar
from django.db.models import Q
from planificaciones.modelos.modelCorrecciones import Correccion
#Correcciones
from planificaciones.formularios.formCorreccion import CorreccionForm
#Comentarios
from planificaciones.formularios.formComentarios import ComentarioForm
from django.contrib.auth.decorators import login_required

##Define request for Asignatura  
@login_required 
def TareasFuncionesIndex(request,id_planificacion):
    planificacion = Planificacion.objects.get(id=id_planificacion) 
    form = DetalleProfesorCatedraForm()
    detalles_profesores_catedra = DetalleProfesorCatedra.objects.filter(planificacion = planificacion) 
    distribucionTareasForm = DistribucionTareasForm(instance=planificacion)
    profesores =  detalles_profesores_catedra.filter(categoria__categoria = "Titular") | detalles_profesores_catedra.filter(categoria__categoria = "Adjunto")
    profesores_auxiliares =  detalles_profesores_catedra.exclude(categoria__categoria = "Titular").exclude(categoria__categoria = "Adjunto")

    mensaje_exito = None
    mensaje_error = None
    #CORRECCIONES
    correcciones = Correccion.objects.filter(Q(planificacion_id = id_planificacion) & Q(seccion = 12)).prefetch_related('comentarios')
    existen_correcciones_pendientes = None
    #Forms Correcciones y Comentarios
    correccionForm = CorreccionForm()
    comentarioForm = ComentarioForm()
    
    for item in correcciones:
        print(item.estado)
        if(item.estado == "G"):
            existen_correcciones_pendientes = "Existen correcciones pendientes de resolver"

    if request.method == "POST":  
        tareasFuncionesForm = TareasFuncionesForm(request.POST)  
        if tareasFuncionesForm.is_valid():  
            try:  
                # Creo una instancia y no lo guardo aun
                instance = tareasFuncionesForm.save(commit=False)
                instance.planificacion_id = id_planificacion
                # Guardo el objeto definitivamente
                instance.save()
                mensaje_exito="Se ha guardado la tarea o unidad con exito"  
            except:  
                mensaje_error="No se pudo guardar la tarea o funcion"  
    tareasFuncionesForm = TareasFuncionesForm()
    #CORRECCIONES
    correcciones = Correccion.objects.filter(Q(planificacion_id = id_planificacion) & Q(seccion = 11)).prefetch_related('comentarios')
    existen_correcciones_pendientes = None
    #Forms Correcciones y Comentarios
    correccionForm = CorreccionForm()
    comentarioForm = ComentarioForm()
    
    for item in correcciones:
        print(item.estado)
        if(item.estado == "G"):
            existen_correcciones_pendientes = "Existen correcciones pendientes de resolver"

    context = {
        'planificacion': planificacion,
        'profesores': profesores,
        'profesores_auxiliares': profesores_auxiliares,
        "form": form,
        'distribucionTareasForm': distribucionTareasForm,
        'tareasFuncionesForm':tareasFuncionesForm,
        'correcciones':correcciones,
        #Forms Correcciones
        'correccion_form': correccionForm,
        'comentario_form':comentarioForm,
        #
        'existen_correcciones_pendientes':existen_correcciones_pendientes,
        "mensaje_exito": mensaje_exito,
        "mensaje_error": mensaje_error,
    }

    return render(request,"secciones/distribucion-de-tareas/index.html", context)  


@login_required 
def TareasFuncionesNew(request,id_planificacion):
    if request.method == "POST":  
        tareasFuncionesForm = TareasFuncionesForm(request.POST)  
        if tareasFuncionesForm.is_valid():  
            try:  
                # Creo una instancia y no lo guardo aun
                instance = tareasFuncionesForm.save(commit=False)
                instance.planificacion_id = id_planificacion
                # Guardo el objeto definitivamente
                instance.save()
                mensaje_exito="Se ha guardado la tarea o unidad con exito"  
            except:  
                mensaje_error="No se pudo guardar la tarea o funcion"  

    return redirect(reverse('planificaciones:detallesprofesorcatedra', args=[id_planificacion]) )