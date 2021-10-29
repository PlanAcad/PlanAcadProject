# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelContenido import Contenido
from planificaciones.formularios.formContenido import ContenidoForm


# To show and to add new one
def IndexContenido(request, id_planificacion):   
    planificacion = Planificacion.objects.get(id=id_planificacion)  
    contenidos = Contenido.objects.filter(planificacion=planificacion).order_by('numero_unidad')  
    mensaje_exito = None
    mensaje_error = None
    
    form = ContenidoForm()
    if request.method == 'POST':
        form = ContenidoForm(request.POST)
        if form.is_valid():
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                instance.save()
                    
                mensaje_exito="Añadimos el contenido correctamente."  
                 
            except:  
                mensaje_error = "No pudimos añadir el contenido." 
                print(form.errors)


        else:
            mensaje_error = "No pudimos añadir el contenido." 
            print(form.errors)


    context = {
        'planificacion': planificacion,
        'contenidos': contenidos,
        "form": form,
        "mensaje_exito": mensaje_exito,
        "mensaje_error": mensaje_error,
    }

    return render(request,"secciones/contenido/index.html", context) 



# To show and to add new one
def UpdateContenido(request, id_planificacion, id_contenido):   
    planificacion = Planificacion.objects.get(id=id_planificacion) 
    contenido = Contenido.objects.get(id=id_contenido)  
    form = ContenidoForm(instance=contenido)
    mensaje_exito = None
    mensaje_error = None
    
    if request.method == 'POST':
        form = ContenidoForm(request.POST, instance=contenido)  
        if form.is_valid():
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                instance.save()
                mensaje_exito="Añadimos el contenido correctamente." 

                return redirect('planificaciones:contenido', id_planificacion=id_planificacion)

                 
            except:  
                mensaje_error = "No pudimos añadir el contenido." 
                print(form.errors)


        else:
            mensaje_error = "No pudimos añadir el contenido." 
            print(form.errors)


    context = {
        'planificacion': planificacion,
        'contenido': contenido,
        "form": form,
        "mensaje_exito": mensaje_exito,
        "mensaje_error": mensaje_error,
    }

    return render(request,"secciones/contenido/update.html", context) 



def DeleteContenido(request, id_planificacion, id_contenido):
    mensaje_exito = None
    mensaje_error = None

    if request.method == "POST":
        try:
            contenido = Contenido.objects.get(id=id_contenido)  
            contenido.delete()
            mensaje_exito = "Se ha borrado correctamente."        
        except:
            mensaje_error = "No pudimos borrar correctamente"  
        
        return redirect('planificaciones:contenido', id_planificacion=id_planificacion)