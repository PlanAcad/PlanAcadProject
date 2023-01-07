# Para usar los objetos y/o funciones de 'redirect'  
from datetime import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
import json
from django.db.models import Q
from django.shortcuts import render, redirect
from planificaciones.modelos.modelFechaCalendarioAcademico import FechaCalendarioAcademico  
## import model and form
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelDatosDescriptivos import DatosDescriptivos
from planificaciones.modelos.modelCorrecciones import Correccion
from planificaciones.formularios.formDatosDescriptivos import  DatosDescriptivosForm
from planificaciones.formularios.formCorreccion import CorreccionForm

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
    data = None
    errores = []  
    planificacion = Planificacion.objects.get(id=id_planificacion) 
    datosDescriptivos = DatosDescriptivos.objects.get(id=planificacion.datos_descriptivos_id)
    form = DatosDescriptivosForm(instance = datosDescriptivos)
    #CORRECCIONES
    correcciones = Correccion.objects.filter(Q(planificacion_id = id_planificacion) & Q(seccion = 1)).prefetch_related('comentarios')
    existen_correcciones_pendientes = None
    correccion = CorreccionForm()
    for item in correcciones:
        print(item.estado)
        if(item.estado == "G"):
            existen_correcciones_pendientes = "Existen correcciones pendientes de resolver"
    
    mensaje_exito = None
    mensaje_error = None
    data_json = request.GET.get('data')
    if(data_json):
        data = json.loads(data_json)
    if request.method == 'POST':  
        form = DatosDescriptivosForm(request.POST,instance = datosDescriptivos)
        if form.is_valid():
            try:
                form.save()                            
                mensaje_exito = "Guardamos los cambios correctamente."
               
            except:
                mensaje_error = "No pudimos guardar los cambios."
    #Agregar
    context = {
        'planificacion': planificacion,
        'form': form,
        'correcciones':correcciones,
        'correccion_form': correccion,
        'datosDescriptivos': datosDescriptivos,
        'existen_correcciones_pendientes': existen_correcciones_pendientes,
        'mensaje_exito': mensaje_exito, 
        'mensaje_error': mensaje_error,
        'errores': data
    }

    return render(request, 'secciones/datos-descriptivos.html', context) 

## Estos de abajo no se usan
def DatosDescriptivosView(request):  
    datosDescriptivos = DatosDescriptivos.objects.all()
    return render(request,"profesores/index.html",{'datosDescriptivos':datosDescriptivos})  

def DatosDescriptivosDetailView(request, id):  
    datosDescriptivos = DatosDescriptivos.objects.get(id=id)
    calendario = FechaCalendarioAcademico.objects.filter(ciclo_lectivo=datetime.now().year).filter(nombre_mes=datetime.now().strftime("%B")).exclude(actividad='DN').order_by('fecha')

    return render(request,'profesores/detail.html', {'datosDescriptivos':datosDescriptivos, 'calendario': calendario})  
    
def DatosDescriptivosDestroy(request, id):  
    datosDescriptivos = DatosDescriptivos.objects.get(id=id)  
    datosDescriptivos.delete()  
    return datosDescriptivos("/show")  