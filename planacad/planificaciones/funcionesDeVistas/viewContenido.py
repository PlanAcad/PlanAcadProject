# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelContenido import Contenido
from planificaciones.formularios.formContenido import ContenidoForm
from planificaciones.formularios.formUnidad import UnidadForm
from planificaciones.modelos.modelUnidad import Unidad

#Agregar
from django.db.models import Q
from planificaciones.modelos.modelCorrecciones import Correccion
#Correcciones
from planificaciones.formularios.formCorreccion import CorreccionForm
#Comentarios
from planificaciones.formularios.formComentarios import ComentarioForm
from django.contrib.auth.decorators import login_required

# To show and to add new one
@login_required
def IndexContenido(request, id_planificacion):   
    planificacion = Planificacion.objects.get(id=id_planificacion)  
    contenidos = Contenido.objects.filter(planificacion=planificacion).order_by('id')  
    unidadForm = UnidadForm()
    mensaje_exito = None
    mensaje_error = None
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

    form = ContenidoForm()
    if request.method == 'POST':
        form = ContenidoForm(request.POST)
        if form.is_valid():
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                instance.save()
                    
                mensaje_exito="Añadimos el contenido correctamente."  
                 
            except:  
                mensaje_error = "No pudimos añadir el contenido." 
                print(form.errors)


        else:
            mensaje_error = "No pudimos añadir el contenido." 
            print(form.errors)
    else:
        form.fields['unidad'].queryset = Unidad.objects.filter(planificacion_id=id_planificacion)


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



# To show and to add new one
@login_required
def UpdateContenido(request, id_planificacion, id_contenido):   
    planificacion = Planificacion.objects.get(id=id_planificacion) 
    contenido = Contenido.objects.get(id=id_contenido)  
    form = ContenidoForm(instance=contenido)
    mensaje_exito = None
    mensaje_error = None
    
    if request.method == 'POST':
        form = ContenidoForm(request.POST, instance=contenido)  
        if form.is_valid():
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                instance.save()
                mensaje_exito="Añadimos el contenido correctamente." 

                return redirect('planificaciones:contenido', id_planificacion=id_planificacion)

                 
            except:  
                mensaje_error = "No pudimos añadir el contenido." 
                print(form.errors)


        else:
            mensaje_error = "No pudimos añadir el contenido." 
            print(form.errors)
    else:
        form.fields['unidad'].queryset = Unidad.objects.filter(planificacion_id=id_planificacion)

    context = {
        'planificacion': planificacion,
        'contenido': contenido,
        "form": form,
        "mensaje_exito": mensaje_exito,
        "mensaje_error": mensaje_error,
    }

    return render(request,"secciones/contenido/update.html", context) 


@login_required
def DeleteContenido(request, id_planificacion, id_contenido):
    mensaje_exito = None
    mensaje_error = None

    if request.method == "POST":
        try:
            contenido = Contenido.objects.get(id=id_contenido)  
            contenido.delete()
            mensaje_exito = "Se ha borrado correctamente."        
        except:
            mensaje_error = "No pudimos borrar correctamente"  
        
        return redirect('planificaciones:contenido', id_planificacion=id_planificacion)