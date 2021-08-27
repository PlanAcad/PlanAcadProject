# Para usar los objetos y/o funciones de 'redirect'  
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render, redirect  
## import model and form
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelDatosDescriptivos import DatosDescriptivos
from planificaciones.formularios.formDatosDescriptivos import  DatosDescriptivosForm
##Define request for Asignatura   
def DatosDescriptivosNew(asignatura_id, carrera_id):      
        form = DatosDescriptivos()  
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
def DatosDescriptivosUpdate(request, id_planificacion):  
    planificacion = Planificacion.objects.get(id=id_planificacion)
    datosDescriptivos = DatosDescriptivos.objects.get(id=planificacion.datos_descriptivos_id)
    form = DatosDescriptivosForm(instance = datosDescriptivos)
    mensaje_exito = None
    mensaje_error = None
    
    if request.method == 'POST':  
        form = DatosDescriptivosForm(request.POST,instance = datosDescriptivos)
        if form.is_valid():
            try:
                form.save()                            
                mensaje_exito = "Guardamos los cambios correctamente."
               
            except:
                mensaje_error = "No pudimos guardar los cambios."
    
    return render(request, 'secciones/datos-descriptivos.html', {'planificacion': planificacion,'datosDescriptivos': datosDescriptivos, 'form': form, 'mensaje_exito': mensaje_exito, 'mensaje_error': mensaje_error}) 

## Estos de abajo no se usan
def DatosDescriptivosView(request):  
    datosDescriptivos = DatosDescriptivos.objects.all()
    return render(request,"profesores/index.html",{'datosDescriptivos':datosDescriptivos})  

def DatosDescriptivosDetailView(request, id):  
    datosDescriptivos = DatosDescriptivos.objects.get(id=id)
    return render(request,'profesores/detail.html', {'datosDescriptivos':datosDescriptivos})  
def DatosDescriptivosDestroy(request, id):  
    datosDescriptivos = DatosDescriptivos.objects.get(id=id)  
    datosDescriptivos.delete()  
    return datosDescriptivos("/show")  