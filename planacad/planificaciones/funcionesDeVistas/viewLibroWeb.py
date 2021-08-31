# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formLibroWeb import LibroWebForm
from planificaciones.modelos.modelLibroWeb import LibroWeb 
from planificaciones.modelos.modelPlanificacion import Planificacion 



##Define request for Asignatura   
def LibroWebNew(request,planificacion_id):
    mensaje_exito = None
    mensaje_error = None
    if request.method == "POST":  
        form = LibroWebForm(request.POST)  
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
        form = LibroWebForm()  
    return render(request,'index.html',{'form':form, 'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito}) 
  
def LibroWebView(request,planificacion_id):
    mensaje_error = None
    try:
         planificacion = Planificacion.objects.get(id=planificacion_id)  
         librosWeb = LibroWeb.objects.filter(planificacion = planificacion)       
    except:
         mensaje_error = ""  
    
    return render(request,"secciones/webgrafia.html",{'librosWeb':librosWeb,'mensaje_error': mensaje_error})  
 

def LibroWebDetailView(request, id):
    mensaje_error = None
    try:
         libroWeb = LibroWeb.objects.get(id=id)    
    except:
         mensaje_error = ""   
    return render(request,'secciones/seccion2detail.html', {'libroWeb':libroWeb
    ,'mensaje_error': mensaje_error})  

def LibroWebUpdate(request, id):  
    mensaje_exito = None
    mensaje_error = None
    try:
        libroWeb = LibroWeb.objects.get(id=id)  
        form = LibroWebForm(request.POST, instance = libroWeb)  
        if form.is_valid():  
            try:
                form.save()                            
                mensaje_exito = "Guardamos los cambios correctamente."        
            except:
                mensaje_error = "No pudimos guardar los cambios."
    except:
        mensaje_error = ""
    return render(request, 'edit.html', {'libroWeb': libroWeb,'mensaje_exito': mensaje_exito, 'mensaje_error': mensaje_error})  

def LibroWebDestroy(request, id):
    mensaje_exito = None
    mensaje_error = None
    try:
         libroWeb = LibroWeb.objects.get(id=id)  
         libroWeb.delete()
         mensaje_exito = "Se ha borrado correctamente."        
    except:
         mensaje_error = "No pudimos borrar correctamente"  
      
    return libroWeb("/show",{'mensaje_exito': mensaje_exito, 'mensaje_error': mensaje_error}) 