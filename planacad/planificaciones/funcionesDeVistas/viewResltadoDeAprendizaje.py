# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelResultadoDeAprendizaje import ResultadoDeAprendizaje
from planificaciones.formularios.formResultadoDeAprendizaje import  ResultadoDeAprendizajeForm
##Define request for Resultado de Aprendizaje   
def ResultadoDeAprendizajeNew(request,planificacion_id,asignatura_id):  
    if request.method == "POST":  
        form = ResultadoDeAprendizajeForm(request.POST)  
        if form.is_valid():  
            try:  
                planificacion = Planificacion.objects.get(id=planificacion_id)
                form.planificacion_id=planificacion.id
                asignatura = Asignatura.objects.get(id=asignatura_id)
                form.asignatura_id = asignatura.id
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ResultadoDeAprendizajeForm()  
    return render(request,'index.html',{'form':form}) 

def ResultadoDeAprendizajeViewbyPlanificacion(request,planificacion_id):  
    planificacion = Planificacion.objects.get(id=planificacion_id)
    resultadosDeAprendizajes = ResultadoDeAprendizaje.objects.filter(planificacion=planificacion)
    return render(request,"profesores/index.html",{'resultadosDeAprendizajes':resultadosDeAprendizajes})  

def ResultadoDeAprendizajeViewbyAsignatura(request, asignatura_id):  
    asignatura = Asignatura.objects.get(id=asignatura_id)
    # Obtener materias del profesor
    resultadosDeAprendizajes = ResultadoDeAprendizaje.objects.filter(asignatura=asignatura)
    return render(request,'profesores/detail.html', {'asignatura':asignatura, 'resultadosDeAprendizajes':resultadosDeAprendizajes})  
 
def ResultadoDeAprendizajeUpdate(request, id):  
    resultadoDeAprendizaje = ResultadoDeAprendizaje.objects.get(id=id)  
    form = ResultadoDeAprendizajeForm(request.POST, instance = resultadoDeAprendizaje)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'resultadoDeAprendizaje': resultadoDeAprendizaje})  

def ResultadoDeAprendizajeDestroy(request, id):  
    resultadoDeAprendizaje = ResultadoDeAprendizaje.objects.get(id=id)  
    resultadoDeAprendizaje.delete()  
    return resultadoDeAprendizaje("/show")  