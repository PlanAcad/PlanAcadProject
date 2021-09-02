# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formDetalleProfesorCatedra import DetalleProfesorCatedraForm
from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra
from planificaciones.modelos.modelTareasFunciones import TareasFunciones
from planificaciones.modelos.modelPlanificacion import Planificacion 


##Define request for Asignatura   
def DetalleProfesorCatedraNew(request, id_planificacion):
    mensaje_exito = None
    mensaje_error = None
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = DetalleProfesorCatedra.objects.filter(planificacion = planificacion)
    if request.method == "POST":  
        form = DetalleProfesorCatedraForm(request.POST)  
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                #Guardo
                instance.save()
                mensaje_exito="Añadimos el docente correctamente."  
                 
            except:  
                 mensaje_error = "No pudimos añadir el docente."    
    else:  
        form = DetalleProfesorCatedraForm()  
    return render(request,'secciones/detallesprofesorcatedra.html',{'data':data,'planificacion':planificacion,'form':form, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 
  
def DetallesProfesorCatedraView(request,id):
    mensaje_error = None
    try:
         planificacion = Planificacion.objects.get(id=id)  
         detallesProfesorCatedra = DetalleProfesorCatedra.objects.filter(planificacion = planificacion)       
    except:
         mensaje_error = ""  
    
    return render(request,"secciones/detallesprofesorcatedra.html",{'detallesprofesorcatedra':detallesProfesorCatedra,'mensaje_error': mensaje_error})  
 

def DetalleProfesorCatedraDetailView(request, id):
    mensaje_error = None
    try:
         detalleProfesorCatedra = DetalleProfesorCatedra.objects.get(id=id)
         tareasFunciones = TareasFunciones.objects.filter(detalle_profesor_catedra = detalleProfesorCatedra)       
    except:
         mensaje_error = ""   
    return render(request,'secciones/seccion2detail.html', {'detalle_profesor_catedra':detalleProfesorCatedra
    ,'tareas_funciones':tareasFunciones,'mensaje_error': mensaje_error})  

def DetalleProfesorCatedraUpdate(request, id_planificacion, id_detalleprofesorcatedra):  
    mensaje_exito = None
    mensaje_error = None
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = DetalleProfesorCatedra.objects.get(id=id_detalleprofesorcatedra)
    if request.method == "POST":  
        print(request.POST)
        form = DetalleProfesorCatedraForm(request.POST)  
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                #Guardo
                instance.save()
                mensaje_exito="Guardamos los cambios correctamente."  
                 
            except:  
                 mensaje_error = "No pudimos guardar los cambios."    
    else:  
        form = DetalleProfesorCatedraForm(instance=data)  
    return render(request,'secciones/detallesProfesorCatedraUpdate.html',{'data':data,'planificacion':planificacion,'form':form, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 
  
    

def DetalleProfesorCatedraDestroy(request, id):
    mensaje_exito = None
    mensaje_error = None
    try:
         detalleProfesorCatedra = DetalleProfesorCatedra.objects.get(id=id)  
         detalleProfesorCatedra.delete()
         mensaje_exito = "Se ha borrado correctamente."        
    except:
         mensaje_error = "No pudimos borrar correctamente"  
      
    return detalleProfesorCatedra("/show",{'mensaje_exito': mensaje_exito, 'mensaje_error': mensaje_error}) 