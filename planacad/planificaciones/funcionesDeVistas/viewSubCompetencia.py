# Para usar los objetos y/o funciones de 'redirect'
from planificaciones.modelos.modelCompetencia import Competencia
from django.shortcuts import render, redirect  
from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.contrib import messages
from planificaciones.modelos.modelCorrecciones import Correccion
## import model and form
from planificaciones.formularios.formSubCompetencia import SubCompetenciaForm
from planificaciones.funcionesDeVistas import viewCorreccion
from planificaciones.modelos.modelSubCompetencia import SubCompetencia 
from planificaciones.modelos.modelPlanificacion import Planificacion 
from django.contrib.auth.decorators import login_required

@login_required
def SubCompetenciaNew(request,id_planificacion,id_competencia):
    mensaje_exito = None
    mensaje_error = None
    planificacion = Planificacion.objects.get(id=id_planificacion)
    competencia = Competencia.objects.get(id=id_competencia)
   
    if request.method == "POST":  
        form = SubCompetenciaForm(request.POST)  
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)
                instance.competencia_id=competencia.id
                #Guardo
                instance.save()
                messages.success(request, 'Se ha guardado con éxito')
                return redirect('planificaciones:competenciaUpdate', id_planificacion=id_planificacion,id_competencia=id_competencia)
            except:  
                 mensaje_error = "No pudimos crear correctamente"    
                 messages.error(request, 'La operación falló') 
    else:  
        form = SubCompetenciaForm()
        #CORRECCIONES
        correcciones = Correccion.objects.filter(Q(planificacion_id = id_planificacion) & Q(seccion = 5)).prefetch_related('comentarios')  
        correcciones = viewCorreccion.OrderCorrecciones(correcciones)
    correccionesEnSecciones = viewCorreccion.CorreccionesEnSecciones(id_planificacion)
    return render(request,'secciones/subcompetencias/index.html',{'planificacion':planificacion,'competencia':competencia,'form':form, 'correccionesEnSecciones':correccionesEnSecciones, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 
  
@login_required
def SubCompetenciaUpdate(request, id_planificacion, id_competencia, id_subcompetencia):  
    mensaje_exito = None
    mensaje_error = None
    planificacion = Planificacion.objects.get(id=id_planificacion)
    competencia = Competencia.objects.get(id=id_competencia)
    data = SubCompetencia.objects.get(id=id_subcompetencia)
    if request.method == "POST":  
        form = SubCompetenciaForm(request.POST, instance=data)  
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                #Guardo
                instance.save()
                messages.success(request, 'Se ha guardado con éxito')
                mensaje_exito="Guardamos los cambios correctamente."
                return HttpResponseRedirect(reverse('planificaciones:competenciaUpdate', args=[id_planificacion, id_competencia]))
                
            except:  
                 mensaje_error = "No pudimos guardar los cambios."   
                 messages.error(request, 'La operación falló')  
    else:  
        form = SubCompetenciaForm(instance=data)
        #CORRECCIONES
        correcciones = Correccion.objects.filter(Q(planificacion_id = id_planificacion) & Q(seccion = 5)).prefetch_related('comentarios')  
        correcciones = viewCorreccion.OrderCorrecciones(correcciones)
    correccionesEnSecciones = viewCorreccion.CorreccionesEnSecciones(id_planificacion)
    return render(request,'secciones/subcompetencias/editar.html',{'data':data,'competencia':competencia,'planificacion':planificacion,'form':form, 'correccionesEnSecciones':correccionesEnSecciones, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 
  
@login_required
def SubCompetenciaDestroy(request, id_planificacion, id_competencia, id_subcompetencia):
    mensaje_exito = None
    mensaje_error = None
    if request.method == "POST":
        try:
            subcompetencia = SubCompetencia.objects.get(id=id_subcompetencia)  
            subcompetencia.delete()
            messages.success(request, 'Se ha guardado con éxito')
            mensaje_exito = "Se ha borrado correctamente."        
        except:
            messages.error(request, 'La operación falló')
            mensaje_error = "No pudimos borrar correctamente"  
        
        return HttpResponseRedirect(reverse('planificaciones:competenciaUpdate', args=[id_planificacion, id_competencia]))

@login_required 
def SubCompetenciaDetailView(request, id):
    mensaje_error = None
    subcompetencia = None
    try:
         subcompetencia = SubCompetencia.objects.get(id=id)    
    except:
         mensaje_error = ""   
    return render(request,'secciones/seccion2detail.html', {'subcompetencia':subcompetencia
    ,'mensaje_error': mensaje_error})  
