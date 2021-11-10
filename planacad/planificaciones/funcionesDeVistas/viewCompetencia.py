# Para usar los objetos y/o funciones de 'redirect'

from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formCompetencia import CompetenciaForm
from planificaciones.modelos.modelCompetencia import Competencia
from planificaciones.modelos.modelSubCompetencia import SubCompetencia
from planificaciones.modelos.modelPlanificacion import Planificacion 



def CompetenciaNew(request,id_planificacion):
    mensaje_exito = None
    mensaje_error = None
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = Competencia.objects.filter(planificacion = planificacion)
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
    return render(request,'secciones/competencias/index.html',{'data':data,'planificacion':planificacion,'form':form, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 
  
  
def CompetenciaView(request,id_planificacion):
    mensaje_error = None
    competencias = None
    try:
         planificacion = Planificacion.objects.get(id=id_planificacion)  
         competencias = Competencia.objects.filter(planificacion = planificacion)       
    except:
         mensaje_error = ""  
    
    return render(request,"secciones/",{'competencias':competencias,'mensaje_error': mensaje_error})  

def CompetenciabyTypeView(request,planificacion_id,type):
    mensaje_error = None
    competencias = None
    try:
         planificacion = Planificacion.objects.get(id=planificacion_id)  
         competencias = Competencia.objects.filter(planificacion = planificacion).filter(tipo_competencia = type)       
    except:
         mensaje_error = ""  
    
    return render(request,"secciones/",{'competencias':competencias,'mensaje_error': mensaje_error})  
 

def CompetenciaDetailView(request, id):
    mensaje_error = None
    competencia = None
    try:
         competencia = Competencia.objects.get(id=id)    
    except:
         mensaje_error = ""   
    return render(request,'secciones/seccion2detail.html', {'competencia':competencia
    ,'mensaje_error': mensaje_error})  

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
    return render(request,'secciones/competencias/editar.html',{'data':data, 'subcompetencias': subcompetencias,'planificacion':planificacion,'form':form, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 
  

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
                 