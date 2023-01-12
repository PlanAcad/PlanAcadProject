# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from planificaciones.formularios.formDetalleProfesorCatedra import DetalleProfesorCatedraForm
from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra  
from planificaciones.modelos.modelPlanificacion import Planificacion
#Agregar
from django.db.models import Q
from planificaciones.modelos.modelCorrecciones import Correccion
#Correcciones
from planificaciones.formularios.formCorreccion import CorreccionForm
#Comentarios
from planificaciones.formularios.formComentarios import ComentarioForm

# To show and to add new one
def DistribucionDeTareas(request, id_planificacion):   
    planificacion = Planificacion.objects.get(id=id_planificacion) 
    detalles_profesores_catedra = DetalleProfesorCatedra.objects.filter(planificacion = planificacion) 

    profesores =  detalles_profesores_catedra.filter(categoria__categoria = "Titular") | detalles_profesores_catedra.filter(categoria__categoria = "Adjunto")
    profesores_auxiliares =  detalles_profesores_catedra.exclude(categoria__categoria = "Titular").exclude(categoria__categoria = "Adjunto")

    mensaje_exito = None
    mensaje_error = None
    #CORRECCIONES
    correcciones = Correccion.objects.filter(Q(planificacion_id = id_planificacion) & Q(seccion = 12)).prefetch_related('comentarios')
    existen_correcciones_pendientes = None
    #Forms Correcciones y Comentarios
    correccionForm = CorreccionForm()
    comentarioForm = ComentarioForm()
    
    for item in correcciones:
        print(item.estado)
        if(item.estado == "G"):
            existen_correcciones_pendientes = "Existen correcciones pendientes de resolver"

    form = DetalleProfesorCatedraForm()
    if request.method == 'POST':
        form = DetalleProfesorCatedraForm(request.POST)
        if form.is_valid():
            try:  
                nombre_profesor = form.cleaned_data["nombre_profesor"]
                apellido_profesor = form.cleaned_data["apellido_profesor"]
                profesor = User.objects.filter(nombre__iexact=nombre_profesor).filter(apellido__iexact=apellido_profesor).first()

                if not profesor:
                    profesor = User.objects.create(nombre=nombre_profesor, apellido=apellido_profesor)

                distribucion_de_tareas = form.save(commit=False)
                distribucion_de_tareas.planificacion_id = planificacion.id
                distribucion_de_tareas.profesor = profesor
                distribucion_de_tareas.save()
                form.save_m2m()

                    
                mensaje_exito="Añadimos el docente correctamente."  
                 
            except:  
                 mensaje_error = "No pudimos añadir el docente." 

        else:
            mensaje_error = "No pudimos añadir el docente." 

    context = {
        'planificacion': planificacion,
        'profesores': profesores,
        'profesores_auxiliares': profesores_auxiliares,
        "form": form,
        'correcciones':correcciones,
        #Forms Correcciones
        'correccion_form': correccionForm,
        'comentario_form':comentarioForm,
        #
        'existen_correcciones_pendientes':existen_correcciones_pendientes,
        "mensaje_exito": mensaje_exito,
        "mensaje_error": mensaje_error,
    }

    return render(request,"secciones/distribucion-de-tareas/index.html", context) 


def UpdateDistribucionDeTareas(request, id_planificacion, id_detalleprofesorcatedra):  
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = DetalleProfesorCatedra.objects.get(id=id_detalleprofesorcatedra)
    form = DetalleProfesorCatedraForm(instance=data)
    mensaje_exito = None
    mensaje_error = None

    if request.method == "POST":  
        form = DetalleProfesorCatedraForm(request.POST, instance=data)  
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                instance.save()
                form.save_m2m()
                mensaje_exito="Guardamos los cambios correctamente."

                return redirect('planificaciones:distribucionDeTareas', id_planificacion=id_planificacion)
                 
            except:  
                mensaje_error = "No pudimos guardar los cambios."  
    
    context = {
        'data':data,
        'planificacion':planificacion,
        'form':form, 
        'mensaje_error': mensaje_error,
        'mensaje_exito':mensaje_exito
    }

    return render(request,'secciones/distribucion-de-tareas/update.html', context) 
    
    

def DeleteDistribucionDeTareas(request, id_planificacion, id_detalleprofesorcatedra):
    mensaje_exito = None
    mensaje_error = None

    if request.method == "POST":
        try:
            detalleProfesorCatedra = DetalleProfesorCatedra.objects.get(id=id_detalleprofesorcatedra)  
            detalleProfesorCatedra.delete()
            mensaje_exito = "Se ha borrado correctamente."        
        except:
            mensaje_error = "No pudimos borrar correctamente"  
        
        return redirect('planificaciones:distribucionDeTareas', id_planificacion=id_planificacion)

