# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formDetalleProfesorCatedra import DetalleProfesorCatedraForm
from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra
from planificaciones.modelos.modelCategoria import Categoria
from planificaciones.modelos.modelDedicacion import Dedicacion
from planificaciones.modelos.modelSituacion import Situacion
from planificaciones.modelos.modelTareasFunciones import TareasFunciones

##Define request for Asignatura   
def NewDetalleProfesorCatedra(request,categoria_id,dedicacion_id,situacion_id):  
    form = DetalleProfesorCatedra()  
    # check whether it's valid:

    print("form valid")
    # Asigno la asignatura y carrera, no hace falta ir a buscar el objeto
    categoria = Categoria.objects.get(id=categoria_id)
    form.categoria_id = categoria.id
    dedicacion = Dedicacion.objects.get(id=dedicacion_id)
    form.dedicacion_id = dedicacion.id
    situacion = Situacion.objects.get(id=situacion_id)
    form.situacion_id = situacion.id
    # Guardo el objeto definitivamente
    form.save()
    # redirect to a new URL:
    return  form

def DetallesProfesorCatedraView(request,seccion2_id):
    #seccion2 = Seccion2.objects.get(id=seccion2_id)  
    #detallesProfesorCatedra = DetalleProfesorCatedra.objects.get(id=seccion2.detalleprofesorcatedra_id)  
    #return render(request,"profesores/index.html",{'detallesProfesorCatedra':detallesProfesorCatedra})  
    return
def DetalleProfesorCatedraDetailView(request, id):  
    detalleProfesorCatedra = DetalleProfesorCatedra.objects.get(id=id)
    detalleProfesorCatedra.situacion = Situacion.objects.get(id=detalleProfesorCatedra.situacion_id)
    detalleProfesorCatedra.categoria = Situacion.objects.get(id=detalleProfesorCatedra.categoria_id)
    detalleProfesorCatedra.dedicacion = Situacion.objects.get(id=detalleProfesorCatedra.dedicacion_id)
    tareasFunciones = TareasFunciones.objects.filter(detalleProfesorCatedra = detalleProfesorCatedra)
    return render(request,'profesores/detail.html', {'detalleProfesorCatedra':detalleProfesorCatedra,
                                                    'tareasfunciones':tareasFunciones})  
 
def DetalleProfesorCatedraUpdate(request, id):  
    detalleProfesorCatedra = DetalleProfesorCatedra.objects.get(id=id)  
    form = DetalleProfesorCatedraForm(request.POST, instance = detalleProfesorCatedra)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'detalleProfesorCatedra': detalleProfesorCatedra})  

def DetalleProfesorCatedraDestroy(request, id):  
    detalleProfesorCatedra = DetalleProfesorCatedra.objects.get(id=id)  
    detalleProfesorCatedra.delete()  
    return detalleProfesorCatedra("/show") 