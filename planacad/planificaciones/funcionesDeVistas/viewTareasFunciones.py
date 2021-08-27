# Para usar los objetos y/o funciones de 'redirect'
from planificaciones.modelos.modelCategoria import Categoria
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formTareasFunciones import TareasFuncionesForm
from planificaciones.modelos.modelTareasFunciones import TareasFunciones
from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra

##Define request for Asignatura   
def TareasFuncionesNew(request,categoria_id,detalle_profesor_catedra_id):
      form = TareasFuncionesForm(request.POST)
        # check whether it's valid:
      if form.is_valid():
            print("form valid")
            # Creo una instancia y no lo guardo aun
            instance = form.save(commit=False)
            # Asigno la asignatura, no hace falta ir a buscar el objeto
            categoria = Categoria.objects.get(id=categoria_id)
            instance.categoria_id = categoria.id
            detalleprofesorcatedra = DetalleProfesorCatedra.objects.get(id=detalle_profesor_catedra_id)
            instance.detalle_profesor_catedra.add(detalleprofesorcatedra)
            # Guardo el objeto definitivamente
            instance.save()
      else:
         form = TareasFuncionesForm()
      return render(request, 'planificacion/index.html', {'form': form})

def TareasFuncionesView(request,categoria_id):  
    situaciones = TareasFunciones.objects.get(categoria_id=categoria_id)  
    return render(request,"",{'situaciones':situaciones})  

def SituacionDetailView(request, id):  
    situacion = TareasFunciones.objects.get(id=id)  
    return render(request,'', {'situacion':situacion})  
 
def SituacionUpdate(request, id):  
    situacion = TareasFunciones.objects.get(id=id)  
    form = TareasFuncionesForm(request.POST, instance = situacion)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'situacion': situacion})  

def SituacionDestroy(request, id):  
    situacion = TareasFunciones.objects.get(id=id)  
    situacion.delete()  
    return situacion("/show")  