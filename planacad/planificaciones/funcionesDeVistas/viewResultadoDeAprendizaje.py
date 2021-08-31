# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelResultadoDeAprendizaje import ResultadoDeAprendizaje
from planificaciones.formularios.formResultadoDeAprendizaje import  ResultadoDeAprendizajeForm
##Define request for Resultado de Aprendizaje   
def ResultadoDeAprendizajeNew(request,planificacion_id,asignatura_id): 
    mensaje_error = None 
    if request.method == "POST":  
        form = ResultadoDeAprendizajeForm(request.POST)  
        if form.is_valid():  
            try:  
                #Obtengo la planificacion
                planificacion = Planificacion.objects.get(id=planificacion_id)
                form.planificacion_id=planificacion.id
                #Obtengo la asignatura
                asignatura = Asignatura.objects.get(id=asignatura_id)
                form.asignatura_id = asignatura.id
                #Guardo
                form.save()  
                return redirect('/show')  
            except:  
                 mensaje_error = "No pudimos crear correctamente"    
    else:  
        form = ResultadoDeAprendizajeForm()  
    return render(request,'index.html',{'form':form, 'mensaje_error': mensaje_error}) 

def ResultadoDeAprendizajeViewbyPlanificacion(request,planificacion_id):
    mensaje_error = None
    try:
         #Obtengo la planificacion
         planificacion = Planificacion.objects.get(id=planificacion_id)
         #Obtengo los resultados de aprendizaje
         resultadosDeAprendizajes = ResultadoDeAprendizaje.objects.filter(planificacion=planificacion) 
    except:
         mensaje_error = "No pudimos obtener los datos correctamente"    
    return render(request,"secciones/resultadosDeAprendizaje.html",{'resultadosDeAprendizajes':resultadosDeAprendizajes, 'mensaje_error': mensaje_error})  

def ResultadoDeAprendizajeViewbyAsignatura(request, asignatura_id): 
    mensaje_error = None 
    try:
         #Obtengo la asignatura
         asignatura = Asignatura.objects.get(id=asignatura_id)
         #Obtengo los resultados de aprendizaje
         resultadosDeAprendizajes = ResultadoDeAprendizaje.objects.filter(asignatura=asignatura)
    except:
         mensaje_error = "No pudimos obtener los datos correctamente" 
    return render(request,'profesores/detail.html', {'asignatura':asignatura, 'resultadosDeAprendizajes':resultadosDeAprendizajes, 'mensaje_error': mensaje_error})  
 
def ResultadoDeAprendizajeUpdate(request, id):  
    mensaje_exito = None
    mensaje_error = None
    resultadoDeAprendizaje = ResultadoDeAprendizaje.objects.get(id=id)  
    form = ResultadoDeAprendizajeForm(request.POST, instance = resultadoDeAprendizaje)  
    if form.is_valid():
     try:
         form.save()                            
         mensaje_exito = "Guardamos los cambios correctamente." 
     except:
         mensaje_error = "No pudimos guardar los cambios."

    return render(request, 'edit.html', {'resultadoDeAprendizaje': resultadoDeAprendizaje,'mensaje_exito': mensaje_exito, 'mensaje_error': mensaje_error})  

def ResultadoDeAprendizajeDestroy(request, id):
    mensaje_exito = None
    mensaje_error = None  
    resultadoDeAprendizaje = ResultadoDeAprendizaje.objects.get(id=id)
    try:
         resultadoDeAprendizaje.delete()                           
         mensaje_exito = "Se ha borrado correctamente."   
    except:
         mensaje_error = "No pudimos borrar correctamente"  
     
    return resultadoDeAprendizaje("/show", {'mensaje_exito': mensaje_exito, 'mensaje_error': mensaje_error})  