# Para usar los objetos y/o funciones de 'redirect'
from planificaciones.modelos.modelCategoria import Categoria
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formTareasFunciones import TareasFuncionesForm
from planificaciones.modelos.modelTareasFunciones import TareasFunciones
from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra

##Define request for Asignatura   
def TareasFuncionesNew(request,categoria_id,detalle_profesor_catedra_id):
    mensaje_exito = None
    mensaje_error = None
    if request.method == "POST":  
        form = TareasFuncionesForm(request.POST)  
        if form.is_valid():  
            try:  
                # Creo una instancia y no lo guardo aun
                instance = form.save(commit=False)
                # Asigno la asignatura, no hace falta ir a buscar el objeto
                categoria = Categoria.objects.get(id=categoria_id)
                instance.categoria_id = categoria.id
                detalleprofesorcatedra = DetalleProfesorCatedra.objects.get(id=detalle_profesor_catedra_id)
                instance.detalle_profesor_catedra.add(detalleprofesorcatedra)
                # Guardo el objeto definitivamente
                instance.save()
                mensaje_exito=""  
            except:  
                mensaje_error=""  
    else:
        form = TareasFuncionesForm()
    return render(request, 'planificacion/index.html', {'form': form,'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito})

def TareasFuncionesView(request,categoria_id):
    mensaje_exito = None
    mensaje_error = None
    try:
         tareasFunciones = TareasFunciones.objects.filter(categoria_id=categoria_id)  
    except:
         mensaje_error = ""  
    return render(request,"",{'tareasFunciones':tareasFunciones,'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito})  

def TareasFuncionesDetailView(request, id):
    mensaje_exito = None
    mensaje_error = None
    try:
         tareasFunciones = TareasFunciones.objects.get(id=id)  
    except:
         mensaje_error = ""  
    return render(request,'', {'tareasFunciones':tareasFunciones,'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito})  
 
def SituacionUpdate(request, id):
    mensaje_exito = None
    mensaje_error = None
    try:
         tareasFunciones = TareasFunciones.objects.get(id=id)  
         form = TareasFuncionesForm(request.POST, instance = tareasFunciones)  
         if form.is_valid():  
            form.save()
            mensaje_exito=""
         else:
               mensaje_error = ""
    except:
         mensaje_error = ""    
    return render(request, 'edit.html', {'tareasFunciones': tareasFunciones,'mensaje_error': mensaje_error,
    'mensaje_exito':mensaje_exito})  

def SituacionDestroy(request, id):
    mensaje_exito = None
    mensaje_error = None
    try:
         tareasFunciones = TareasFunciones.objects.get(id=id)  
         tareasFunciones.delete() 
         mensaje_exito = ""
    except:
         mensaje_error = ""  
      
    return tareasFunciones("/show")  