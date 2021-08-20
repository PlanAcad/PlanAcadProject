# Para usar los objetos y/o funciones de 'redirect'  
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render, redirect  
## import model and form
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelSeccion1 import Seccion1
from planificaciones.formularios.formSeccion1 import  Seccion1Form
##Define request for Asignatura   
def Seccion1New(asignatura_id, carrera_id):      
        form = Seccion1()  
        # Asigno la asignatura y carrera, no hace falta ir a buscar el objeto
        form.asignatura_id = asignatura_id
        form.carrera_id = carrera_id
        # Guardo el objeto definitivamente
        form.save()
        # redirect to a new URL:
        return  form


# Esto muestro en /seccion1
# Si es un POST actualiza
# Si es un GET mando el form y los datos actuales
def Seccion1Update(request, id_planificacion):  
    planificacion = Planificacion.objects.get(id=id_planificacion)
    seccion1 = Seccion1.objects.get(id=planificacion.seccion1_id)
    form = Seccion1Form(request.POST, instance = seccion1)
    
    if request.method == 'POST':  
        if form.is_valid():  
            form.save()  
            # Vuelvo a la misma página, parece que ambos funcionan
            #return redirect('planificaciones:seccion1', id_planificacion)
            return HttpResponseRedirect(request.path_info)
    return render(request, 'secciones/seccion1.html', {'planificacion': planificacion,'seccion1': seccion1, 'form': form}) 

## Estos de abajo no se usan
def Seccion1View(request):  
    secciones1 = Seccion1.objects.all()
    return render(request,"profesores/index.html",{'secciones1':secciones1})  

def Seccion1DetailView(request, id):  
    seccion1 = Seccion1.objects.get(id=id)
    return render(request,'profesores/detail.html', {'seccion1':seccion1})  
def Seccion1Destroy(request, id):  
    seccion1 = Seccion1.objects.get(id=id)  
    seccion1.delete()  
    return seccion1("/show")  