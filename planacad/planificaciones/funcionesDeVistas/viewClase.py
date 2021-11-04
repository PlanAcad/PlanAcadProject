# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect
import planificaciones
from planificaciones.modelos.modelAsignatura import Asignatura  
## import model and form
from planificaciones.modelos.modelClase import Clase
from planificaciones.modelos.modelContenido import Contenido
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelProfesor import Profesor
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.formularios.formClase import  ClaseForm
from planificaciones.formularios.formResultadoDeAprendizaje import  ResultadoDeAprendizaje

##Define request for Resultado de Aprendizaje   
def ClaseNew(request,id_planificacion): 
    mensaje_exito=None
    mensaje_error=None
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = Clase.objects.filter(planificacion=planificacion)
    if request.method == "POST":  
        form = ClaseForm(request.POST)
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                instance.save()
                mensaje_exito="Añadimos la clase correctamente."  
            except:  
                 mensaje_error = "No pudimos añadir la clase."    
    else:  
        form = ClaseForm()
        form.fields['profesor_a_cargo'].queryset = Profesor.objects.filter(asignatura__id = planificacion.asignatura_id)
        form.fields['unidad_tematica_o_tema'].queryset = Contenido.objects.filter(planificacion = planificacion)
        form.fields['resultado_de_aprendizaje'].queryset = ResultadoDeAprendizaje.objects.filter(planificacion = planificacion)
         
    return render(request,'secciones/cronograma/index.html',{'planificacion':planificacion,'data':data,'form':form, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 
  

def ClasesView(request,planificacion_id):
    mensaje_error = None
    try:
         #Obtengo la planificacion
         planificacion = Planificacion.objects.get(id=planificacion_id)
         #Obtengo los resultados de aprendizaje
         clases = Clase.objects.filter(planificacion=planificacion) 
    except:
         mensaje_error = "No pudimos obtener los datos correctamente"    
    return render(request,"secciones/cronograma/.html",{'clases':clases, 'mensaje_error': mensaje_error})  

def ClaseViewDetail(request,clase_id): 
    mensaje_error = None 
    try:
         #Obtengo la clase
         clase = Clase.objects.get(id=clase_id)
    except:
         mensaje_error = "No pudimos obtener los datos correctamente" 
    return render(request,'secciones/cronograma/.html', {'clase':clase, 'mensaje_error': mensaje_error})  


def ResultadoDeAprendizajeUpdate(request, id_planificacion, id_resultadodeaprendizaje):  
    mensaje_exito = None
    mensaje_error = None
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = Clase.objects.filter(planificacion=planificacion)
    if request.method == "POST":  
        form = ClaseForm(request.POST, instance = data)  
        if form.is_valid():  
            try: 
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                #Guardo
                instance.save()
                mensaje_exito="Guardamos los cambios correctamente."
                return redirect('planificaciones:', id_planificacion=id_planificacion)
                 
            except:  
                 mensaje_error = "No pudimos guardar los cambios."    
    else:  
        form = ClaseForm(instance=data)
        form.fields['profesor_a_cargo'].queryset = Profesor.objects.filter(asignatura__id = planificacion.asignatura_id)
        form.fields['unidad_tematica_o_tema'].queryset = Contenido.objects.filter(planificacion = planificacion)
        form.fields['resultado_de_aprendizaje'].queryset = ResultadoDeAprendizaje.objects.filter(planificacion = planificacion)  
    return render(request,'secciones/cronograma/.html',{'data':data,'planificacion':planificacion,'form':form, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 
  
    

def ClaseDestroy(request,id_planificacion ,clase_id):
    mensaje_exito = None
    mensaje_error = None
    if request.method == "POST":
        try:
            clase = Clase.objects.get(id=clase_id)  
            clase.delete()
            mensaje_exito = "Se ha borrado correctamente."        
        except:
            mensaje_error = "No pudimos borrar correctamente"  
        
        return redirect('planificaciones:', id_planificacion=id_planificacion)
                 