# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect
from planificaciones.modelos.modelAsignatura import Asignatura  
## import model and form
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelResultadoAprendizaje import ResultadoDeAprendizaje
from planificaciones.modelos.modelResultadoDeAprendizajeAnterior import ResultadoDeAprendizajeAnterior
from planificaciones.formularios.formResultadoDeAprendizajeAnterior import  ResultadoDeAprendizajeAnteriorForm
from planificaciones.formularios.formResultadoDeAprendizaje import  ResultadoDeAprendizajeForm

from django.db.models import F
from django.db.models import Q
from planificaciones.modelos.modelCorrecciones import Correccion
#Correcciones
from planificaciones.formularios.formCorreccion import CorreccionForm
#Comentarios
from planificaciones.formularios.formComentarios import ComentarioForm
from django.contrib.auth.decorators import login_required

@login_required
def ResultadoDeAprendizajeNewFirstPlanificacion(request,id_planificacion): 
    planificacion = Planificacion.objects.get(id=id_planificacion)
    if request.method == "POST":  
        formresultadoAprendizaje = ResultadoDeAprendizajeForm(request.POST)
        formresultadoAprendizaje.fields['asignatura'].queryset = Asignatura.objects.filter(carrera=planificacion.asignatura.carrera).distinct().exclude(id = planificacion.asignatura_id)
        
        if formresultadoAprendizaje.is_valid():  
            try:  
                instance = formresultadoAprendizaje.save(commit=False)
                instance.save()
                instance.save_m2m()
            except:  
                 mensaje_error = "No pudimos añadir el resultado de aprendizaje."  

    return redirect('planificaciones:resultadosDeAprendizajes', id_planificacion=id_planificacion)

##Define request for Resultado de Aprendizaje   
@login_required
def ResultadoDeAprendizajeAnteriorNew(request,id_planificacion): 
    mensaje_exito=None
    mensaje_error=None
    resultados=None
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = ResultadoDeAprendizajeAnterior.objects.filter(planificacion=planificacion)
    #CORRECCIONES
    correcciones = Correccion.objects.filter(Q(planificacion_id = id_planificacion) & Q(seccion = 4)).prefetch_related('comentarios')
    existen_correcciones_pendientes = None
    #Forms Correcciones y Comentarios
    correccionForm = CorreccionForm()
    comentarioForm = ComentarioForm()
    
    for item in correcciones:
        if(item.estado == "G"):
            existen_correcciones_pendientes = "Existen correcciones pendientes de resolver"
    formresultadoAprendizaje = ResultadoDeAprendizajeForm()
    if request.method == "POST":  
        form = ResultadoDeAprendizajeAnteriorForm(request.POST)
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                instance.save()
                mensaje_exito="Añadimos el resultado de aprendizaje correctamente."  
            except:  
                 mensaje_error = "No pudimos añadir el resultado de aprendizaje."    
      
    form = ResultadoDeAprendizajeAnteriorForm()
    form.fields['asignatura'].queryset = Asignatura.objects.filter(carrera=planificacion.asignatura.carrera).distinct().exclude(id = planificacion.asignatura_id)
        

    #Agregar
    context = {
        'planificacion': planificacion,
        'resultados':resultados,
        'data':data,
        'form':form,
        'formresultadoAprendizaje':formresultadoAprendizaje,
        'correcciones':correcciones,
        #Forms Correcciones
        'correccion_form': correccionForm,
        'comentario_form':comentarioForm,
        #
        'existen_correcciones_pendientes':existen_correcciones_pendientes,
        'mensaje_exito': mensaje_exito, 
        'mensaje_error': mensaje_error
    }  
    return render(request,'secciones/resultadosDeAprendizaje.html',context) 
  
@login_required
def ResultadosDeAprendizajePorAsignatura(request):
    asignatura_id=request.GET.get('asignatura')
    resultados = ResultadoDeAprendizaje.objects.none()
    if(asignatura_id):
        planificacionesAsignatura = Planificacion.objects.filter(asignatura_id=asignatura_id).filter(eliminada= False).filter(estado='A').order_by('fecha_creacion')
        lastPlanificacionAsignatura = planificacionesAsignatura.last()  
        if(lastPlanificacionAsignatura):
            resultados = ResultadoDeAprendizaje.objects.filter(asignatura_id=asignatura_id).filter(planificacion_id = lastPlanificacionAsignatura.id).order_by('resultado')    
        else:
            resultados = ResultadoDeAprendizaje.objects.filter(asignatura_id=asignatura_id).order_by('resultado')
    
    return render(request, 'secciones/resultado-de-aprendizaje-anterior/dropdown-ra-anteriores-options.html', {'resultados': resultados})

@login_required
def ResultadoDeAprendizajeAnteriorViewbyPlanificacion(request,planificacion_id):
    mensaje_error = None
    try:
         #Obtengo la planificacion
         planificacion = Planificacion.objects.get(id=planificacion_id)
         #Obtengo los resultados de aprendizaje
         resultadosDeAprendizajes = ResultadoDeAprendizajeAnterior.objects.filter(planificacion=planificacion) 
    except:
         mensaje_error = "No pudimos obtener los datos correctamente"    
    return render(request,"secciones/resultadosDeAprendizaje.html",{'resultadosDeAprendizajes':resultadosDeAprendizajes, 'mensaje_error': mensaje_error})  


@login_required
def ResultadoDeAprendizajeAnteriorUpdate(request, id_planificacion, id_resultadodeaprendizaje):  
    mensaje_exito = None
    mensaje_error = None
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = ResultadoDeAprendizajeAnterior.objects.get(id=id_resultadodeaprendizaje)
    if request.method == "POST":  
        form = ResultadoDeAprendizajeAnteriorForm(request.POST, instance = data)  
        if form.is_valid():  
            try: 
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                #Guardo
                instance.save()
                mensaje_exito="Guardamos los cambios correctamente."
                return redirect('planificaciones:resultadosDeAprendizajes', id_planificacion=id_planificacion)
                 
            except:  
                 mensaje_error = "No pudimos guardar los cambios."    
    else:  
        form = ResultadoDeAprendizajeAnteriorForm(instance = data)
        form.fields['asignatura'].queryset = Asignatura.objects.filter(planificacion__estado='A').distinct().exclude(id = planificacion.asignatura_id)

    return render(request,'secciones/resultadosDeAprendizajeUpdate.html',{'data':data,'planificacion':planificacion,'form':form, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 
  
    
@login_required
def ResultadoDeAprendizajeAnteriorDestroy(request, id_planificacion, id_resultadodeaprendizaje):
    mensaje_exito = None
    mensaje_error = None
    if request.method == "POST":
        try:
            detalleProfesorCatedra = ResultadoDeAprendizajeAnterior.objects.get(id=id_resultadodeaprendizaje)  
            detalleProfesorCatedra.delete()
            mensaje_exito = "Se ha borrado correctamente."        
        except:
            mensaje_error = "No pudimos borrar correctamente"  
        
        return redirect('planificaciones:resultadosDeAprendizajes', id_planificacion=id_planificacion)
                 