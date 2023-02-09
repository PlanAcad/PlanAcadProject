# Para usar los objetos y/o funciones de 'redirect'
from planificaciones.modelos.modelPlanificacion import Planificacion
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formUnidad import UnidadForm
from planificaciones.formularios.formContenido import ContenidoForm
from planificaciones.modelos.modelContenido import Contenido
from planificaciones.modelos.modelUnidad import Unidad
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
def UnidadNew(request,id_planificacion):
    planificacion = Planificacion.objects.get(id = id_planificacion)
    mensaje_exito = None
    mensaje_error = None
    form = ContenidoForm()
    
    if request.method == "POST":  
        unidadForm = UnidadForm(request.POST)  
        if unidadForm.is_valid():  
            try:  
                # Creo una instancia y no lo guardo aun
                instance = unidadForm.save(commit=False)
                instance.planificacion_id = id_planificacion
                # Guardo el objeto definitivamente
                instance.save()
                mensaje_exito="Se ha guardado la unidad con exito"  
            except:  
                mensaje_error="No se pudo guardar la planificacion"  
    else:
        unidadForm = UnidadForm()

    form.fields['unidad'].queryset = Unidad.objects.filter(planificacion_id=id_planificacion)
    contenidos = Contenido.objects.filter(planificacion=planificacion).order_by('id')
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
        'contenidos': contenidos,
        "form": form,
        'formUnidad': unidadForm,
        'correcciones':correcciones,
        #Forms Correcciones
        'correccion_form': correccionForm,
        'comentario_form':comentarioForm,
        #
        'existen_correcciones_pendientes':existen_correcciones_pendientes,
        "mensaje_exito": mensaje_exito,
        "mensaje_error": mensaje_error,
    }

    return render(request,"secciones/contenido/index.html", context) 