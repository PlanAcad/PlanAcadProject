# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
from django.urls import reverse

from django.http import HttpResponseRedirect
## import model and form
from planificaciones.formularios.formDetalleProfesorCatedra import DetalleProfesorCatedraForm
from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra
from planificaciones.modelos.modelTareasFunciones import TareasFunciones
from planificaciones.modelos.modelPlanificacion import Planificacion 


##Define request for Asignatura   
def DetalleProfesorCatedraNew(request, id_planificacion):
    mensaje_exito=None
    mensaje_error=None
    
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = DetalleProfesorCatedra.objects.filter(planificacion = planificacion)
    if request.method == "POST":  
        form = DetalleProfesorCatedraForm(request.POST)  
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                #Guardo
                instance.save()

               # selectedTareas = form.cleaned_data.get('tareas')
                #for tarea in selectedTareas:
                 #   tarea_obj = TareasFunciones.objects.get(id = tarea.id)
                  #  instance.tareas.add(tarea_obj)
                    
                mensaje_exito="Añadimos el docente correctamente."  
                 
            except:  
                 mensaje_error = "No pudimos añadir el docente."    
    else:  
        form = DetalleProfesorCatedraForm()  
    return render(request,'secciones/detallesprofesorcatedra.html',{'data':data,'planificacion':planificacion,'form':form, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 
  

def DetalleProfesorCatedraUpdate(request, id_planificacion, id_detalleprofesorcatedra):  
    mensaje_exito = None
    mensaje_error = None
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = DetalleProfesorCatedra.objects.get(id=id_detalleprofesorcatedra)
    if request.method == "POST":  
        form = DetalleProfesorCatedraForm(request.POST, instance=data)  
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                #Guardo
                instance.save()
                form.save_m2m()
                mensaje_exito="Guardamos los cambios correctamente."
                #return HttpResponseRedirect(reverse('planificaciones:detallesprofesorcatedra', args=[id_planificacion]))
                return redirect('planificaciones:detallesprofesorcatedra', id_planificacion=id_planificacion)
                 
            except:  
                 mensaje_error = "No pudimos guardar los cambios."    
    else:  
        form = DetalleProfesorCatedraForm(instance=data)  
    return render(request,'secciones/detallesProfesorCatedraUpdate.html',{'data':data,'planificacion':planificacion,'form':form, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 
  
    

def DetalleProfesorCatedraDestroy(request, id_planificacion, id_detalleprofesorcatedra):
    mensaje_exito = None
    mensaje_error = None
    if request.method == "POST":
        try:
            detalleProfesorCatedra = DetalleProfesorCatedra.objects.get(id=id_detalleprofesorcatedra)  
            detalleProfesorCatedra.delete()
            mensaje_exito = "Se ha borrado correctamente."        
        except:
            mensaje_error = "No pudimos borrar correctamente"  
        
        return redirect('planificaciones:detallesprofesorcatedra', id_planificacion=id_planificacion)
                 