# Para usar los objetos y/o funciones de 'redirect'
from planificaciones.modelos.modelCompetencia import Competencia
from django.shortcuts import render, redirect  
from django.http import  HttpResponseRedirect
from django.urls import reverse

## import model and form
from planificaciones.formularios.formSubCompetencia import SubCompetenciaForm
from planificaciones.modelos.modelSubCompetencia import SubCompetencia 
from planificaciones.modelos.modelPlanificacion import Planificacion 

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
                return redirect('planificaciones:competencias', id_planificacion=id_planificacion)
            except:  
                 mensaje_error = "No pudimos crear correctamente"    
    else:  
        form = SubCompetenciaForm()  
    return render(request,'secciones/subcompetencias/index.html',{'planificacion':planificacion,'competencia':competencia,'form':form, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 
  
  
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
                mensaje_exito="Guardamos los cambios correctamente."
                return HttpResponseRedirect(reverse('planificaciones:competenciaUpdate', args=[id_planificacion, id_competencia]))
                
            except:  
                 mensaje_error = "No pudimos guardar los cambios."    
    else:  
        form = SubCompetenciaForm(instance=data)  
    return render(request,'secciones/subcompetencias/editar.html',{'data':data,'competencia':competencia,'planificacion':planificacion,'form':form, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 
  

def SubCompetenciaDestroy(request, id_planificacion, id_competencia, id_subcompetencia):
    mensaje_exito = None
    mensaje_error = None
    if request.method == "POST":
        try:
            subcompetencia = SubCompetencia.objects.get(id=id_subcompetencia)  
            subcompetencia.delete()
            mensaje_exito = "Se ha borrado correctamente."        
        except:
            mensaje_error = "No pudimos borrar correctamente"  
        
        return HttpResponseRedirect(reverse('planificaciones:competenciaUpdate', args=[id_planificacion, id_competencia]))

        
def SubCompetenciaDetailView(request, id):
    mensaje_error = None
    subcompetencia = None
    try:
         subcompetencia = SubCompetencia.objects.get(id=id)    
    except:
         mensaje_error = ""   
    return render(request,'secciones/seccion2detail.html', {'subcompetencia':subcompetencia
    ,'mensaje_error': mensaje_error})  
