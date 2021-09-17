# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formUnidad import UnidadForm,Unidad
from planificaciones.modelos.modelPlanificacion import Planificacion 



##Define request for Asignatura   
def UnidadNew(request,planificacion_id):
    mensaje_exito = None
    mensaje_error = None
    if request.method == "POST":  
        form = UnidadForm(request.POST)  
        if form.is_valid():  
            try:
                instance = form.save(commit=False)  
                #Obtengo la planificacion
                planificacion = Planificacion.objects.get(id=planificacion_id)
                instance.planificacion_id=planificacion.id
                #Guardo
                form.save()
                mensaje_exito=""  
                return redirect('/show')  
            except:  
                 mensaje_error = "No pudimos crear correctamente"    
    else:  
        form = UnidadForm()  
    return render(request,'index.html',{'form':form, 'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito}) 
  
def UnidadView(request,id_planificacion):
    mensaje_error = None
    unidades = None
    try:
         planificacion = Planificacion.objects.get(id=id_planificacion)  
         unidades = Unidad.objects.filter(planificacion = planificacion)       
    except:
         mensaje_error = ""  
    
    return render(request,"secciones/",{'unidades':unidades,'mensaje_error': mensaje_error})  

def UnidadDetailView(request, id):
    mensaje_error = None
    unidad = None
    try:
         unidad = Unidad.objects.get(id=id)    
    except:
         mensaje_error = ""   
    return render(request,'secciones/seccion2detail.html', {'unidad':unidad
    ,'mensaje_error': mensaje_error})  

def UnidadUpdate(request, id,planificacion_id):  
    mensaje_exito = None
    mensaje_error = None
    unidad = None
    try:
        unidad = Unidad.objects.get(id=id)
        planificacion = Planificacion.objects.get(id = planificacion_id)  
        unidad.planificacion_id = planificacion.id
        form = UnidadForm(request.POST, instance = unidad)  
        if form.is_valid():  
            try:
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                form.save()                            
                mensaje_exito = "Guardamos los cambios correctamente."        
            except:
                mensaje_error = "No pudimos guardar los cambios."
    except:
        mensaje_error = ""
    return render(request, 'edit.html', {'unidad': unidad,'mensaje_exito': mensaje_exito, 'mensaje_error': mensaje_error})  

def UnidadDestroy(request, id):
    mensaje_exito = None
    mensaje_error = None
    unidad = None
    try:
         unidad = Unidad.objects.get(id=id)
         unidad.delete()
         mensaje_exito = "Se ha borrado correctamente."        
    except:
         mensaje_error = "No pudimos borrar correctamente"  
      
    return unidad("/show",{'mensaje_exito': mensaje_exito, 'mensaje_error': mensaje_error}) 