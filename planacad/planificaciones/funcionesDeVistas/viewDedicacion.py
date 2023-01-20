# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formDedicacion import DedicacionForm
from planificaciones.modelos.modelDedicacion import Dedicacion
from django.contrib.auth.decorators import login_required


##Define request for Asignatura   
@login_required
def DedicacionNew(request):
    mensaje_exito = None
    mensaje_error = None  
    if request.method == "POST":  
        form = DedicacionForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()
                mensaje_exito=""  
            except:  
                mensaje_error=""  
    else:  
        form = DedicacionForm()  
    return render(request,'index.html',{'form':form,'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito}) 

@login_required
def DedicacionesView(request):
    mensaje_error = None
    try:
         dedicaciones = Dedicacion.objects.all()  
    except:
         mensaje_error = ""  
    return render(request,"",{'dedicaciones':dedicaciones,'mensaje_error': mensaje_error})  

@login_required
def DedicacionDetailView(request, id):
    mensaje_error = None
    try:
         dedicacion = Dedicacion.objects.get(id=id)   
    except:
         mensaje_error = ""  
    return render(request,'', {'dedicacion':dedicacion,'mensaje_error': mensaje_error})  
 
@login_required
def DedicacionUpdate(request, id):
    mensaje_exito = None
    mensaje_error = None
    try:
         dedicacion = Dedicacion.objects.get(id=id)  
         form = DedicacionForm(request.POST, instance = dedicacion)  
         if form.is_valid():  
            form.save()
            mensaje_exito=""
         else:
               mensaje_error = ""
    except:
         mensaje_error = ""  
    return render(request, 'edit.html', {'dedicacion': dedicacion,'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito})  

@login_required
def DedicacionDestroy(request, id):
    mensaje_exito = None
    mensaje_error = None
    try:
         dedicacion = Dedicacion.objects.get(id=id)  
         dedicacion.delete()
         mensaje_exito = ""
    except:
         mensaje_error = ""  
      
    return dedicacion("/show",{'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito})  