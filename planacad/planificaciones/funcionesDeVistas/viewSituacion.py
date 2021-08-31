# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formSituacion import SituacionForm
from planificaciones.modelos.modelSituacion import Situacion
##Define request for Asignatura   
def SituacionNew(request):
    mensaje_exito = None
    mensaje_error = None  
    if request.method == "POST":  
        form = SituacionForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()
                mensaje_exito=""  
            except:  
                mensaje_error=""  
    else:  
        form = SituacionForm()  
    return render(request,'index.html',{'form':form,'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito}) 

def SituacionesView(request):
    mensaje_error = None
    try:
         situaciones = Situacion.objects.all()  
    except:
         mensaje_error = ""  
      
    return render(request,"",{'situaciones':situaciones,'mensaje_error': mensaje_error})  

def SituacionDetailView(request, id):
    mensaje_error = None  
    try:
         situacion = Situacion.objects.get(id=id)    
    except:
         mensaje_error = ""  
    
    return render(request,'', {'situacion':situacion,'mensaje_error': mensaje_error})  
 
def SituacionUpdate(request, id):
    mensaje_exito = None
    mensaje_error = None  
    try:
         situacion = Situacion.objects.get(id=id)  
         form = SituacionForm(request.POST, instance = situacion)  
         if form.is_valid():  
            form.save()
            mensaje_exito=""
         else:
               mensaje_error = ""
    except:
         mensaje_error = ""  
    return render(request, 'edit.html', {'situacion': situacion,'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito})  

def SituacionDestroy(request, id):
    mensaje_exito = None
    mensaje_error = None
    try:
         situacion = Situacion.objects.get(id=id)  
         situacion.delete()
         mensaje_exito = ""
    except:
         mensaje_error = ""  
      
    return situacion("/show",{'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito})  