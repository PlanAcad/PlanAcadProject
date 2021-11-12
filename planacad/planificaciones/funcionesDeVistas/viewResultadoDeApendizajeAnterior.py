# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect
from planificaciones.modelos.modelAsignatura import Asignatura  
## import model and form
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelResultadoAprendizaje import ResultadoDeAprendizaje
from planificaciones.modelos.modelResultadoDeAprendizajeAnterior import ResultadoDeAprendizajeAnterior
from planificaciones.formularios.formResultadoDeAprendizajeAnterior import  ResultadoDeAprendizajeAnteriorForm
from django.db.models import F

##Define request for Resultado de Aprendizaje   
def ResultadoDeAprendizajeAnteriorNew(request,id_planificacion): 
    mensaje_exito=None
    mensaje_error=None
    resultados=None
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = ResultadoDeAprendizajeAnterior.objects.filter(planificacion=planificacion)
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
    else:  
        form = ResultadoDeAprendizajeAnteriorForm()
        form.fields['asignatura'].queryset = Asignatura.objects.exclude(id = planificacion.asignatura_id)
        ##form.fields['resultado'].queryset = ResultadoDeAprendizaje.objects.filter(asignatura_id=request.GET.get('asignatura')).order_by('resultado')
    return render(request,'secciones/resultadosDeAprendizaje.html',{'data':data,'resultados':resultados,'planificacion':planificacion,'form':form, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 
  
def ResultadosDeAprendizajePorAsignatura(request):
    asignatura_id=request.GET.get('asignatura')
    resultados = ResultadoDeAprendizaje.objects.filter(asignatura_id=asignatura_id).order_by('resultado')
    return render(request, 'secciones/resultado-de-aprendizaje-anterior/dropdown-ra-anteriores-options.html', {'resultados': resultados})

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
        form = ResultadoDeAprendizajeAnteriorForm()
        form.fields['asignatura'].queryset = Asignatura.objects.exclude(id = planificacion.asignatura_id) 
    return render(request,'secciones/resultadosDeAprendizajeUpdate.html',{'data':data,'planificacion':planificacion,'form':form, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 
  
    

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
                 