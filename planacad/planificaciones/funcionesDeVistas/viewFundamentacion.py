# Para usar los objetos y/o funciones de 'redirect'  
from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from planificaciones.modelos.modelFechaCalendarioAcademico import FechaCalendarioAcademico  
## import model and form
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelFundamentacion import Fundamentacion
from planificaciones.formularios.formFundamentacion import  FundamentacionForm
##Define request for Asignatura   
def FundamentacionNew():      
        form = Fundamentacion()
        # Guardo el objeto definitivamente
        form.save()
        # redirect to a new URL:
        return  form

##Este no se deberia usar pero bueno
def FundamentacionView(request):  
    fundamentacion = Fundamentacion.objects.all()
    return render(request,"profesores/index.html",{'fundamentacion':fundamentacion})  

def FundamentacionDetailView(request, id):  
    fundamentacion = Fundamentacion.objects.get(id=id)
    calendario = FechaCalendarioAcademico.objects.filter(ciclo_lectivo=datetime.now().year).filter(nombre_mes=datetime.now().strftime("%B")).exclude(actividad='DN').order_by('fecha')

    return render(request,'profesores/detail.html', {'fundamentacion':fundamentacion, 'calendario': calendario})  
 
def FundamentacionUpdate(request, id_planificacion):  
    planificacion = Planificacion.objects.get(id=id_planificacion)
    fundamentacion = Fundamentacion.objects.get(id=planificacion.fundamentacion_id)
    form = FundamentacionForm(instance = fundamentacion)
    mensaje_exito = None
    mensaje_error = None
    
    if request.method == 'POST':  
        form = FundamentacionForm(request.POST,instance = fundamentacion)
        if form.is_valid():
            try:
                form.save()                            
                mensaje_exito = "Guardamos los cambios correctamente."
               
            except:
                mensaje_error = "No pudimos guardar los cambios."
    
    return render(request, 'secciones/fundamentacion.html', {'planificacion': planificacion,'fundamentacion': fundamentacion, 'form': form, 'mensaje_exito': mensaje_exito, 'mensaje_error': mensaje_error})  

def FundamentacionDestroy(request, id):  
    fundamentacion = Fundamentacion.objects.get(id=id)  
    fundamentacion.delete()  
    return fundamentacion("/show")  