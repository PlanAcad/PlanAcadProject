# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formLibro import LibroForm
from planificaciones.modelos.modelLibro import Libro 
from planificaciones.modelos.modelPlanificacion import Planificacion 



##Define request for Asignatura   
def LibroNew(request,planificacion_id):
    mensaje_exito = None
    mensaje_error = None
    if request.method == "POST":  
        form = LibroForm(request.POST)  
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
        form = LibroForm()  
    return render(request,'index.html',{'form':form, 'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito}) 
  
def LibrosView(request,planificacion_id):
    mensaje_error = None
    libros = None
    try:
         planificacion = Planificacion.objects.get(id=planificacion_id)  
         libros = Libro.objects.filter(planificacion = planificacion)       
    except:
         mensaje_error = ""  
    
    return render(request,"secciones/bibliografia.html",{'libros':libros,'mensaje_error': mensaje_error})  
 

def LibroDetailView(request, id):
    mensaje_error = None
    libro = None
    try:
         libro = Libro.objects.get(id=id)    
    except:
         mensaje_error = ""   
    return render(request,'secciones/seccion2detail.html', {'libro':libro
    ,'mensaje_error': mensaje_error})  

def LibroUpdate(request, id):  
    mensaje_exito = None
    mensaje_error = None
    libro = None
    try:
        libro = Libro.objects.get(id=id)  
        form = LibroForm(request.POST, instance = libro)  
        if form.is_valid():  
            try:
                form.save()                            
                mensaje_exito = "Guardamos los cambios correctamente."        
            except:
                mensaje_error = "No pudimos guardar los cambios."
    except:
        mensaje_error = ""
    return render(request, 'edit.html', {'libro': libro,'mensaje_exito': mensaje_exito, 'mensaje_error': mensaje_error})  

def LibroDestroy(request, id):
    mensaje_exito = None
    mensaje_error = None
    libro = None
    try:
         libro = Libro.objects.get(id=id)  
         libro.delete()
         mensaje_exito = "Se ha borrado correctamente."        
    except:
         mensaje_error = "No pudimos borrar correctamente"  
      
    return libro("/show",{'mensaje_exito': mensaje_exito, 'mensaje_error': mensaje_error}) 