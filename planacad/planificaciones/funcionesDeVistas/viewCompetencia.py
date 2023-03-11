# Para usar los objetos y/o funciones de 'redirect'

from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formCompetencia import CompetenciaForm
from planificaciones.modelos.modelCompetencia import Competencia
from planificaciones.modelos.modelSubCompetencia import SubCompetencia
from planificaciones.modelos.modelPlanificacion import Planificacion 
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
def CompetenciaNew(request,id_planificacion):
    mensaje_exito = None
    mensaje_error = None
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = Competencia.objects.filter(planificacion = planificacion)
         #CORRECCIONES
    correcciones = Correccion.objects.filter(Q(planificacion_id = id_planificacion) & Q(seccion = 5)).prefetch_related('comentarios')
    correccionesEnSecciones = viewCorreccion.CorreccionesEnSecciones(id_planificacion)
    existen_correcciones_pendientes = None
    #Forms Correcciones y Comentarios
    correccionForm = CorreccionForm()
    comentarioForm = ComentarioForm()
    
    for item in correcciones:
        print(item.estado)
        if(item.estado == "G"):
            existen_correcciones_pendientes = "Existen correcciones pendientes de resolver"

    if request.method == "POST":  
        form = CompetenciaForm(request.POST)  
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                #Guardo
                instance.save()
                return redirect('planificaciones:competencias', id_planificacion=id_planificacion)
            except:  
                 mensaje_error = "No pudimos crear correctamente"    
    else:  
        form = CompetenciaForm()
    competenciaAnterior = None
    ultimaPlanificacionAprobada = Planificacion.objects.filter(asignatura = planificacion.asignatura).filter(estado = 'A').last()
    if (ultimaPlanificacionAprobada):
        competenciaAnterior = Competencia.objects.filter(planificacion = ultimaPlanificacionAprobada)
    #Agregar
    context = {
        'planificacion': planificacion,
        'data':data,
        'form':form,
        'correcciones':correcciones,
        'competenciaAnterior':competenciaAnterior,
        #Forms Correcciones
        'correccion_form': correccionForm,
        'comentario_form':comentarioForm,
        'correccionesEnSecciones':correccionesEnSecciones,
        #
        'existen_correcciones_pendientes':existen_correcciones_pendientes,
        'mensaje_exito': mensaje_exito, 
        'mensaje_error': mensaje_error
    }  
    return render(request,'secciones/competencias/index.html',context) 
  
@login_required
def CompetenciaView(request,id_planificacion):
    mensaje_error = None
    competencias = None
    try:
         planificacion = Planificacion.objects.get(id=id_planificacion)  
         competencias = Competencia.objects.filter(planificacion = planificacion)       
    except:
         mensaje_error = ""  
    
    return render(request,"secciones/",{'competencias':competencias,'mensaje_error': mensaje_error})  

@login_required
def CargarCompetencia(request,id_planificacion):
    if request.method == "POST": 
        opcion_seleccionada = request.POST.getlist('competencias', None)
        if(opcion_seleccionada):
            for comp in opcion_seleccionada:
                if(comp):
                    competencia = Competencia.objects.get(id = str(comp))
                    if(competencia):
                        competenciaNueva = Competencia()
                        competenciaNueva.tipo_competencia = competencia.tipo_competencia
                        competenciaNueva.descripcion = competencia.descripcion
                        competenciaNueva.planificacion_id = id_planificacion
                        competenciaNueva.save()
                        for subComp in competencia.subcompetencia_set.all():
                            if(subComp):
                                subCompeteneciaNueva = SubCompetencia()
                                subCompeteneciaNueva.descripcion = subComp.descripcion
                                subCompeteneciaNueva.competencia = competenciaNueva
                                subCompeteneciaNueva.save()
    return redirect('planificaciones:competencias', id_planificacion=id_planificacion)


@login_required
def CompetenciabyTypeView(request,planificacion_id,type):
    mensaje_error = None
    competencias = None
    try:
         planificacion = Planificacion.objects.get(id=planificacion_id)  
         competencias = Competencia.objects.filter(planificacion = planificacion).filter(tipo_competencia = type)       
    except:
         mensaje_error = ""  
    
    return render(request,"secciones/",{'competencias':competencias,'mensaje_error': mensaje_error})  
 

@login_required
def CompetenciaDetailView(request, id):
    mensaje_error = None
    competencia = None
    try:
         competencia = Competencia.objects.get(id=id)    
    except:
         mensaje_error = ""   
    return render(request,'secciones/seccion2detail.html', {'competencia':competencia
    ,'mensaje_error': mensaje_error})  

@login_required
def CompetenciaUpdate(request, id_planificacion, id_competencia):  
    mensaje_exito = None
    mensaje_error = None
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = Competencia.objects.get(id=id_competencia)
    subcompetencias = SubCompetencia.objects.filter(competencia = data)
    if request.method == "POST":  
        form = CompetenciaForm(request.POST, instance=data)  
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                #Guardo
                instance.save()
                mensaje_exito="Guardamos los cambios correctamente."
                return redirect('planificaciones:competencias', id_planificacion=id_planificacion)
                 
            except:  
                 mensaje_error = "No pudimos guardar los cambios."    
    else:  
        form = CompetenciaForm(instance=data)  
        correccionesEnSecciones = viewCorreccion.CorreccionesEnSecciones(id_planificacion)
    return render(request,'secciones/competencias/editar.html',{'data':data, 'subcompetencias': subcompetencias,'planificacion':planificacion,'form':form,'correccionesEnSecciones':correccionesEnSecciones, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 
  
@login_required
def CompetenciaDestroy(request, id_planificacion, id_competencia):
    mensaje_exito = None
    mensaje_error = None
    if request.method == "POST":
        try:
            competencia = Competencia.objects.get(id=id_competencia)  
            competencia.delete()
            mensaje_exito = "Se ha borrado correctamente."        
        except:
            mensaje_error = "No pudimos borrar correctamente"  
        
        return redirect('planificaciones:competencias', id_planificacion=id_planificacion)
                 