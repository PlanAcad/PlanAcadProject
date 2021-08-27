# Para usar los objetos y/o funciones de 'redirect'  
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelSeccion3 import Seccion3
from planificaciones.formularios.formSeccion3 import  Seccion3Form
##Define request for Asignatura   
def Seccion3New():      
        form = Seccion3()
        # Guardo el objeto definitivamente
        form.save()
        # redirect to a new URL:
        return  form

##Este no se deberia usar pero bueno
def Seccion3View(request):  
    secciones3 = Seccion3.objects.all()
    return render(request,"profesores/index.html",{'secciones3':secciones3})  

def Seccion3DetailView(request, id):  
    seccione3 = Seccion3.objects.get(id=id)
    return render(request,'profesores/detail.html', {'seccione3':seccione3})  
 
def Seccion3Update(request, id_planificacion):  
    planificacion = Planificacion.objects.get(id=id_planificacion)
    seccion3 = Seccion3.objects.get(id=planificacion.seccion3_id)
    form = Seccion3Form(instance = seccion3)
    mensaje_exito = None
    mensaje_error = None
    
    if request.method == 'POST':  
        form = Seccion3Form(request.POST,instance = seccion3)
        if form.is_valid():
            try:
                form.save()                            
                mensaje_exito = "Guardamos los cambios correctamente."
               
            except:
                mensaje_error = "No pudimos guardar los cambios."
    
    return render(request, 'secciones/seccion3.html', {'planificacion': planificacion,'seccion3': seccion3, 'form': form, 'mensaje_exito': mensaje_exito, 'mensaje_error': mensaje_error})  

def Seccion3Destroy(request, id):  
    seccione3 = Seccion3.objects.get(id=id)  
    seccione3.delete()  
    return seccione3("/show")  