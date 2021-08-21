# Para usar los objetos y/o funciones de 'redirect'
from planificaciones.modelos.modelCategoria import Categoria
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formTareasFunciones import TareasFuncionesForm
from planificaciones.modelos.modelTareasFunciones import TareasFunciones
##Define request for Asignatura   
def NewTareasFunciones(request,categoria_id):
      form = TareasFuncionesForm(request.POST)
        # check whether it's valid:
      if form.is_valid():
            print("form valid")
            # Creo una instancia y no lo guardo aun
            instance = form.save(commit=False)
            # Asigno la asignatura, no hace falta ir a buscar el objeto
            categoria = Categoria.objects.get(id=categoria_id)
            instance.categoria_id = categoria.id
            # Guardo el objeto definitivamente
            instance.save()
      else:
         form = TareasFuncionesForm()
      return render(request, 'planificacion/index.html', {'form': form})

def TareasFuncionesView(request):  
    situaciones = TareasFunciones.objects.all()  
    return render(request,"profesores/index.html",{'situaciones':situaciones})  

def SituacionDetailView(request, id):  
    situacion = TareasFunciones.objects.get(id=id)  
    return render(request,'profesores/detail.html', {'situacion':situacion})  
 
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