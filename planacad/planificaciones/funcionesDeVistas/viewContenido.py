# Para usar los objetos y/o funciones de 'redirect'
from planificaciones.modelos.modelUnidad import Unidad
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formContenido import ContenidoForm
from planificaciones.modelos.modelContenido import Contenido 
from planificaciones.modelos.modelPlanificacion import Planificacion 



##Define request for Asignatura   
def ContenidoNew(request,unidad_id):
    mensaje_exito = None
    mensaje_error = None
    if request.method == "POST":  
        form = ContenidoForm(request.POST)  
        if form.is_valid():  
            try: 
                instance = form.save(commit=False) 
                #Obtengo la planificacion
                unidad = Unidad.objects.get(id=unidad_id)
                instance.unidad_id=unidad.id
                #Guardo
                form.save()
                mensaje_exito=""  
                return redirect('/show')  
            except:  
                 mensaje_error = "No pudimos crear correctamente"    
    else:  
        form = ContenidoForm()  
    return render(request,'index.html',{'form':form, 'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito}) 
  
def ContenidoView(request,id_planificacion):
    mensaje_error = None
    contenidos = None
    try:
         planificacion = Planificacion.objects.get(id=id_planificacion)  
         unidades = Unidad.objects.filter(planificacion = planificacion)
         contenidos = Contenido.objects.filter(unidad__in = unidades)
    except:
         mensaje_error = "errar"  
    
    return render(request,"secciones/unidades.html",{'contenidos':contenidos,'mensaje_error': mensaje_error})  

def ContenidobyUnidadView(request,unidad_id):
    mensaje_error = None
    contenidos = None
    try: 
         unidad = Unidad.objects.get(id = unidad_id)
         contenidos = Contenido.objects.filter(unidad=unidad)       
    except:
         mensaje_error = ""  
    
    return render(request,"secciones/",{'contenidos':contenidos,'mensaje_error': mensaje_error})  
 

def ContenidoDetailView(request, id):
    mensaje_error = None
    subcompetencia = None
    try:
         contenido = Contenido.objects.get(id=id)    
    except:
         mensaje_error = ""   
    return render(request,'secciones/seccion2detail.html', {'contenido':contenido
    ,'mensaje_error': mensaje_error})  

def ContenidoUpdate(request, id,unidad_id):  
    mensaje_exito = None
    mensaje_error = None
    contenido = None
    try:
        unidad = Unidad.objects.get(id=unidad_id)
        contenido = Contenido.objects.get(id=id)
        contenido.unidad_id = unidad.id  
        form = ContenidoForm(request.POST, instance = contenido)  
        if form.is_valid():  
            try:
                instance = form.save(commit=False)
                instance.unidad_id=unidad.id
                form.save()                            
                mensaje_exito = "Guardamos los cambios correctamente."        
            except:
                mensaje_error = "No pudimos guardar los cambios."
    except:
        mensaje_error = ""
    return render(request, 'edit.html', {'contenido': contenido,'mensaje_exito': mensaje_exito, 'mensaje_error': mensaje_error})  

def ContenidoDestroy(request, id):
    mensaje_exito = None
    mensaje_error = None
    contenido = None
    try:
         contenido = Unidad.objects.get(id=id)  
         contenido.delete()
         mensaje_exito = "Se ha borrado correctamente."        
    except:
         mensaje_error = "No pudimos borrar correctamente"  
      
    return contenido("/show",{'mensaje_exito': mensaje_exito, 'mensaje_error': mensaje_error}) 