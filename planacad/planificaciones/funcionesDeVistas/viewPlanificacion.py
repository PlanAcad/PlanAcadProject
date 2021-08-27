# Para usar los objetos y/o funciones de 'redirect'

from django.shortcuts import render, redirect  
from django.http import HttpResponseRedirect

## import model and form
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelCarrera import Carrera
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.formularios.formPlanificacion import PlanificacionForm
from planificaciones.funcionesDeVistas import viewDatosDescriptivos
from planificaciones.funcionesDeVistas import viewFundamentacion

##Define request for Planificacion   
def PlanificacionNew(request, asignatura_id):  
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PlanificacionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print("form valid")
            # Creo una instancia y no lo guardo aun
            instance = form.save(commit=False)
            # Asigno la asignatura, no hace falta ir a buscar el objeto
            instance.asignatura_id = asignatura_id
            # Obtengo el id de carrera 
            asignatura = Asignatura.objects.get(id=asignatura_id) 

            # Creo secciones vacías           
            datosDescriptivos = viewDatosDescriptivos.DatosDescriptivosNew(asignatura_id=asignatura_id, carrera_id=asignatura.carrera_id)
            fundamentacion = viewFundamentacion.FundamentacionNew()
            
            # Vinculo los ids
            instance.datosDescriptivos_id = datosDescriptivos.id
            instance.fundamentacion_id = fundamentacion.id
            
            # Guardo el objeto definitivamente
            instance.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/asignaturas/'+str(asignatura_id))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = PlanificacionForm()
    return render(request, 'planificacion/index.html', {'form': form})

def PlanificacionesView(request,idAsignatura):
    #Obtengo la asignatura
    asignatura = Asignatura.objects.get(id=idAsignatura)   
    #Busco las planificaciones de esa asignatura
    planificaciones = Planificacion.objects.filter(asignatura=asignatura)
    return render(request,"planificacion/index.html",{'planificaciones':planificaciones})  

def PlanificacionDetailView(request, id): 
    planificacion = Planificacion.objects.get(id=id)
    return render(request,'planificacion/detail.html', {'planificacion':planificacion})  
 
def PlanificacionUpdate(request, id):  
    planificacion = Planificacion.objects.get(id=id)  
    form = PlanificacionForm(request.POST, instance = planificacion)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'planificacion': planificacion})  

def PlanificacionDestroy(request, id):  
    planificacion = Planificacion.objects.get(id=id)  
    planificacion.delete()  
    return planificacion("/show")  