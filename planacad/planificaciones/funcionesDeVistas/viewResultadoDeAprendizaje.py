# Para usar los objetos y/o funciones de 'redirect'
from datetime import datetime
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelFechaCalendarioAcademico import FechaCalendarioAcademico
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelResultadoAprendizaje import ResultadoDeAprendizaje
from planificaciones.formularios.formResultadoDeAprendizaje import  ResultadoDeAprendizajeForm
from django.contrib.auth.decorators import login_required


##Define request for Resultado de Aprendizaje   
@login_required
def ResultadoDeAprendizajeNew(request,id_planificacion): 
    mensaje_exito=None
    mensaje_error=None
    
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = ResultadoDeAprendizaje.objects.filter(planificacion=planificacion)
    if request.method == "POST":  
        form = ResultadoDeAprendizajeForm(request.POST)
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                instance.save()
                instance.save_m2m()
                mensaje_exito="Añadimos el resultado de aprendizaje correctamente."  
            except:  
                 mensaje_error = "No pudimos añadir el resultado de aprendizaje."    
    else:  
        form = ResultadoDeAprendizajeForm()
        form.fields['asignatura'].queryset = Asignatura.objects.filter(id = planificacion.asignatura_id)  
    return render(request,'secciones/resultadosDeAprendizaje.html',{'data':data,'planificacion':planificacion,'form':form, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 

@login_required
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

@login_required
def ResultadoDeAprendizajeViewbyAsignatura(request, asignatura_id): 
    mensaje_error = None 
    try:
         #Obtengo la asignatura
         asignatura = Asignatura.objects.get(id=asignatura_id)
         #Obtengo los resultados de aprendizaje
         resultadosDeAprendizajes = ResultadoDeAprendizaje.objects.filter(asignatura=asignatura)
         calendario = FechaCalendarioAcademico.objects.filter(ciclo_lectivo=datetime.now().year).filter(nombre_mes=datetime.now().strftime("%B")).exclude(actividad='DN').order_by('fecha')

    except:
         mensaje_error = "No pudimos obtener los datos correctamente" 
    return render(request,'profesores/detail.html', {'asignatura':asignatura, 'resultadosDeAprendizajes':resultadosDeAprendizajes, 'mensaje_error': mensaje_error, 'calendario': calendario})  

@login_required
def ResultadoDeAprendizajeUpdate(request, id_planificacion, id_resultadodeaprendizaje):  
    mensaje_exito = None
    mensaje_error = None
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = ResultadoDeAprendizaje.objects.get(id=id_resultadodeaprendizaje)
    if request.method == "POST":  
        form = ResultadoDeAprendizajeForm(request.POST, instance = data)  
        if form.is_valid():  
            try: 
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                #Guardo
                instance.save()
                instance.save_m2m()
                mensaje_exito="Guardamos los cambios correctamente."
                return redirect('planificaciones:resultadosDeAprendizajes', id_planificacion=id_planificacion)
                 
            except:  
                 mensaje_error = "No pudimos guardar los cambios."    
    else:  
        form = ResultadoDeAprendizajeForm(instance=data)  
    return render(request,'secciones/resultadosDeAprendizajeUpdate.html',{'data':data,'planificacion':planificacion,'form':form, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 
  
    
@login_required
def ResultadoDeAprendizajeDestroy(request, id_planificacion, id_resultadodeaprendizaje):
    mensaje_exito = None
    mensaje_error = None
    if request.method == "POST":
        try:
            detalleProfesorCatedra = ResultadoDeAprendizaje.objects.get(id=id_resultadodeaprendizaje)  
            detalleProfesorCatedra.delete()
            mensaje_exito = "Se ha borrado correctamente."        
        except:
            mensaje_error = "No pudimos borrar correctamente"  
        
        return redirect('planificaciones:resultadosDeAprendizajes', id_planificacion=id_planificacion)
                 