# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelWebgrafia import Webgrafia
from planificaciones.formularios.formWebgrafia import WebgrafiaForm
#Agregar
from django.db.models import Q
from planificaciones.modelos.modelCorrecciones import Correccion
from planificaciones.funcionesDeVistas import viewCorreccion
#Correcciones
from planificaciones.formularios.formCorreccion import CorreccionForm
#Comentarios
from planificaciones.formularios.formComentarios import ComentarioForm
from django.contrib.auth.decorators import login_required


# To show and to add new one
@login_required
def IndexWebgrafia(request, id_planificacion):   
    planificacion = Planificacion.objects.get(id=id_planificacion)  
    webgrafias = Webgrafia.objects.filter(planificacion=planificacion)  
    mensaje_exito = None
    mensaje_error = None
    #CORRECCIONES
    correcciones = Correccion.objects.filter(Q(planificacion_id = id_planificacion) & Q(seccion = 10)).prefetch_related('comentarios')
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
        form = WebgrafiaForm(request.POST)
        if form.is_valid():
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                instance.save()
                    
                mensaje_exito="Añadimos la webgrafía correctamente."  
                 
            except:  
                mensaje_error = "No pudimos añadir la webgrafía." 
                print(form.errors)


        else:
            mensaje_error = "No pudimos añadir la webgrafía." 
            print(form.errors)

    form = WebgrafiaForm()
    context = {
        'planificacion': planificacion,
        'webgrafias': webgrafias,
        "form": form,
        'correcciones':correcciones,
        #Forms Correcciones
        'correccion_form': correccionForm,
        'comentario_form':comentarioForm,
        'correccionesEnSecciones':correccionesEnSecciones,
        #
        'existen_correcciones_pendientes':existen_correcciones_pendientes,
        "mensaje_exito": mensaje_exito,
        "mensaje_error": mensaje_error,
    }

    return render(request,"secciones/webgrafia/index.html", context) 



# To show and to add new one
@login_required
def UpdateWebgrafia(request, id_planificacion, id_webgrafia):   
    planificacion = Planificacion.objects.get(id=id_planificacion) 
    webgrafia = Webgrafia.objects.get(id=id_webgrafia)  
    form = WebgrafiaForm(instance=webgrafia)
    mensaje_exito = None
    mensaje_error = None
    
    if request.method == 'POST':
        form = WebgrafiaForm(request.POST, instance=webgrafia)  
        if form.is_valid():
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                instance.save()
                mensaje_exito="Añadimos la webgrafía correctamente." 

                return redirect('planificaciones:webgrafia', id_planificacion=id_planificacion)

                 
            except:  
                mensaje_error = "No pudimos añadir la webgrafía." 
                print(form.errors)


        else:
            mensaje_error = "No pudimos añadir la webgrafía." 
            print(form.errors)

    correcciones = Correccion.objects.filter(Q(planificacion_id = id_planificacion) & Q(seccion = 10)).prefetch_related('comentarios')
    correcciones = viewCorreccion.OrderCorrecciones(correcciones)
    correccionesEnSecciones = viewCorreccion.CorreccionesEnSecciones(id_planificacion)
    context = {
        'planificacion': planificacion,
        'webgrafia': webgrafia,
        "form": form,
        'correccionesEnSecciones':correccionesEnSecciones,
        "mensaje_exito": mensaje_exito,
        "mensaje_error": mensaje_error,
    }

    return render(request,"secciones/webgrafia/update.html", context) 


@login_required
def DeleteWebgrafia(request, id_planificacion, id_webgrafia):
    mensaje_exito = None
    mensaje_error = None

    if request.method == "POST":
        try:
            webgrafia = Webgrafia.objects.get(id=id_webgrafia)  
            webgrafia.delete()
            mensaje_exito = "Se ha borrado correctamente."        
        except:
            mensaje_error = "No pudimos borrar correctamente"  
        
        return redirect('planificaciones:webgrafia', id_planificacion=id_planificacion)