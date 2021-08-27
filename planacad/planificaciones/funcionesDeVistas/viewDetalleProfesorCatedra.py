# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formDetalleProfesorCatedra import DetalleProfesorCatedraForm
from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra
from planificaciones.modelos.modelTareasFunciones import TareasFunciones
from planificaciones.modelos.modelPlanificacion import Planificacion 


##Define request for Asignatura   
def DetalleProfesorCatedraNew(request,planificacion_id):  
    form = DetalleProfesorCatedra()  
    # check whether it's valid:
    print("form valid")
    # Asigno la asignatura y carrera, no hace falta ir a buscar el objeto
    planificacion = Planificacion.objects.get(id=planificacion_id)
    form.planificacion_id = planificacion.id
    # Guardo el objeto definitivamente
    form.save()
    # redirect to a new URL:
    return  form

def DetallesProfesorCatedraView(request,id):
    planificacion = Planificacion.objects.get(id=id)  
    detallesprofesorcatedra = DetalleProfesorCatedra.objects.filter(planificacion = planificacion)
    return render(request,"secciones/detallesProfesorCatedra.html",{'detallesprofesorcatedra':detallesprofesorcatedra})  
 

def DetalleProfesorCatedraDetailView(request, id):  
    detalleprofesorcatedra = DetalleProfesorCatedra.objects.get(id=id)
    tareasfunciones = TareasFunciones.objects.filter(detalle_profesor_catedra = detalleprofesorcatedra)
    return render(request,'secciones/seccion2detail.html', {'detalle_profesor_catedra':detalleprofesorcatedra
    ,'tareas_funciones':tareasfunciones})  

def DetalleProfesorCatedraUpdate(request, id):  
    detalleprofesorcatedra = DetalleProfesorCatedra.objects.get(id=id)  
    form = DetalleProfesorCatedraForm(request.POST, instance = detalleprofesorcatedra)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'detalleprofesorcatedra': detalleprofesorcatedra})  

def DetalleProfesorCatedraDestroy(request, id):  
    detalleprofesorcatedra = DetalleProfesorCatedra.objects.get(id=id)  
    detalleprofesorcatedra.delete()  
    return detalleprofesorcatedra("/show") 