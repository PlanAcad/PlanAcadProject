# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect
from planificaciones.modelos.modelAsignatura import Asignatura  
## import model and form
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelResultadoDeAprendizajeAnterior import ResultadoDeAprendizajeAnteriorPrimerNivel
from planificaciones.formularios.formResultadoDeAprendizajeAnterior import  ResultadoDeAprendizajeAnteriorPrimerNivelForm

from django.db.models import F
from django.db.models import Q
from planificaciones.modelos.modelCorrecciones import Correccion
#Correcciones
from planificaciones.formularios.formCorreccion import CorreccionForm
from planificaciones.funcionesDeVistas import viewCorreccion
#Comentarios
from planificaciones.formularios.formComentarios import ComentarioForm
from django.contrib.auth.decorators import login_required


##Define request for Resultado de Aprendizaje   
@login_required
def ResultadoDeAprendizajeAnteriorPrimerNivelNew(request,id_planificacion): 
    mensaje_exito=None
    mensaje_error=None
    resultados=None
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = ResultadoDeAprendizajeAnteriorPrimerNivel.objects.filter(planificacion=planificacion)
    #CORRECCIONES
    correcciones = Correccion.objects.filter(Q(planificacion_id = id_planificacion) & Q(seccion = 4)).prefetch_related('comentarios')
    correccionesEnSecciones = viewCorreccion.CorreccionesEnSecciones(id_planificacion)
    existen_correcciones_pendientes = None
    #Forms Correcciones y Comentarios
    correccionForm = CorreccionForm()
    comentarioForm = ComentarioForm()
    
    for item in correcciones:
        if(item.estado == "G"):
            existen_correcciones_pendientes = "Existen correcciones pendientes de resolver"
    form = ResultadoDeAprendizajeAnteriorPrimerNivelForm()
    if request.method == "POST":  
        form = ResultadoDeAprendizajeAnteriorPrimerNivelForm(request.POST)
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                instance.save()
                mensaje_exito="Añadimos el resultado de aprendizaje correctamente."  
            except:  
                 mensaje_error = "No pudimos añadir el resultado de aprendizaje."    
      
        
    #Agregar
    context = {
        'planificacion': planificacion,
        'resultados':resultados,
        'data':data,
        'form':form,
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
    return render(request,'secciones/resultadosDeAprendizajePrimerNivel.html',context) 
  

@login_required
def ResultadoDeAprendizajeAnteriorPrimerNivelUpdate(request, id_planificacion, id_resultadodeaprendizaje):  
    mensaje_exito = None
    mensaje_error = None
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = ResultadoDeAprendizajeAnteriorPrimerNivel.objects.get(id=id_resultadodeaprendizaje)
    if request.method == "POST":  
        form = ResultadoDeAprendizajeAnteriorPrimerNivelForm(request.POST, instance = data)  
        if form.is_valid():  
            try: 
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                #Guardo
                instance.save()
                mensaje_exito="Guardamos los cambios correctamente."
                return redirect('planificaciones:resultadosDeAprendizajesAnteriorPrimerNivel', id_planificacion=id_planificacion)
                 
            except:  
                 mensaje_error = "No pudimos guardar los cambios."    
    else:  
        form = ResultadoDeAprendizajeAnteriorPrimerNivelForm(instance = data)
        correccionesEnSecciones = viewCorreccion.CorreccionesEnSecciones(id_planificacion)

    return render(request,'secciones/resultadosDeAprendizajeUpdatePrimerNivel.html',{'data':data,'planificacion':planificacion,'form':form,'correccionesEnSecciones':correccionesEnSecciones, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 
  
    
@login_required
def ResultadoDeAprendizajeAnteriorPrimerNivelDestroy(request, id_planificacion, id_resultadodeaprendizaje):
    if request.method == "POST":
        try:
            data = ResultadoDeAprendizajeAnteriorPrimerNivel.objects.get(id=id_resultadodeaprendizaje)  
            data.delete()
        except:
            print("error")
            mensaje_error = "No pudimos borrar correctamente"  
        
        return redirect('planificaciones:resultadosDeAprendizajesAnteriorPrimerNivel', id_planificacion=id_planificacion)
                 