# Para usar los objetos y/o funciones de 'redirect'
from planificaciones.modelos.modelCompetencia import Competencia
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formSubCompetencia import SubCompetenciaForm
from planificaciones.modelos.modelSubCompetencia import SubCompetencia 
from planificaciones.modelos.modelPlanificacion import Planificacion 



##Define request for Asignatura   
def CompetenciaNew(request,planificacion_id):
    mensaje_exito = None
    mensaje_error = None
    if request.method == "POST":  
        form = SubCompetenciaForm(request.POST)  
        if form.is_valid():  
            try:  
                #Obtengo la planificacion
                planificacion = Planificacion.objects.get(id=planificacion_id)
                form.planificacion_id=planificacion.id
                #Guardo
                form.save()
                mensaje_exito=""  
                return redirect('/show')  
            except:  
                 mensaje_error = "No pudimos crear correctamente"    
    else:  
        form = SubCompetenciaForm()  
    return render(request,'index.html',{'form':form, 'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito}) 
  
def SubCompetenciaView(request,id_planificacion):
    mensaje_error = None
    subcompetencias = None
    try:
         planificacion = Planificacion.objects.get(id=id_planificacion)  
         competencias = Competencia.objects.filter(planificacion = planificacion)
         subcompetencias = SubCompetencia.objects.filter(competencia__in = competencias)
    except:
         mensaje_error = "errar"  
    
    return render(request,"secciones/competencias.html",{'subcompetencias':subcompetencias,'mensaje_error': mensaje_error})  

def SubCompetenciabyCompetenciaView(request,competencia_id):
    mensaje_error = None
    subcompetencias = None
    try: 
         competencia = Competencia.objects.get(id = competencia_id)
         subcompetencias = SubCompetencia.objects.filter(competencia=competencia)       
    except:
         mensaje_error = ""  
    
    return render(request,"secciones/",{'subcompetencias':subcompetencias,'mensaje_error': mensaje_error})  
 

def SubCompetenciaDetailView(request, id):
    mensaje_error = None
    subcompetencia = None
    try:
         subcompetencia = SubCompetencia.objects.get(id=id)    
    except:
         mensaje_error = ""   
    return render(request,'secciones/seccion2detail.html', {'subcompetencia':subcompetencia
    ,'mensaje_error': mensaje_error})  

def SubCompetenciaUpdate(request, id):  
    mensaje_exito = None
    mensaje_error = None
    subcompetencia = None
    try:
        subcompetencia = SubCompetencia.objects.get(id=id)  
        form = SubCompetenciaForm(request.POST, instance = subcompetencia)  
        if form.is_valid():  
            try:
                form.save()                            
                mensaje_exito = "Guardamos los cambios correctamente."        
            except:
                mensaje_error = "No pudimos guardar los cambios."
    except:
        mensaje_error = ""
    return render(request, 'edit.html', {'subcompetencia': subcompetencia,'mensaje_exito': mensaje_exito, 'mensaje_error': mensaje_error})  

def SubCompetenciaDestroy(request, id):
    mensaje_exito = None
    mensaje_error = None
    subcompetencia = None
    try:
         subcompetencia = SubCompetencia.objects.get(id=id)  
         subcompetencia.delete()
         mensaje_exito = "Se ha borrado correctamente."        
    except:
         mensaje_error = "No pudimos borrar correctamente"  
      
    return subcompetencia("/show",{'mensaje_exito': mensaje_exito, 'mensaje_error': mensaje_error}) 