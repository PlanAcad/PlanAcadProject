# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelBibliografia import Bibliografia
from planificaciones.formularios.formBibliografia import BibliografiaForm


# To show and to add new one
def IndexBibliografia(request, id_planificacion):   
    planificacion = Planificacion.objects.get(id=id_planificacion)  
    bibliografias = Bibliografia.objects.filter(planificacion=planificacion)  
    mensaje_exito = None
    mensaje_error = None
    
    form = BibliografiaForm()
    if request.method == 'POST':
        form = BibliografiaForm(request.POST)
        if form.is_valid():
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                instance.save()
                    
                mensaje_exito="Añadimos la bibliografía correctamente."  
                 
            except:  
                 mensaje_error = "No pudimos añadir la bibliografía." 

        else:
            mensaje_error = "No pudimos añadir la bibliografía." 

    context = {
        'planificacion': planificacion,
        'bibliografias': bibliografias,
        "form": form,
        "mensaje_exito": mensaje_exito,
        "mensaje_error": mensaje_error,
    }

    return render(request,"secciones/bibliografia/index.html", context) 



# To show and to add new one
def UpdateBibliografia(request, id_planificacion, id_bibliografia):   
    planificacion = Planificacion.objects.get(id=id_planificacion) 
    bibliografia = Bibliografia.objects.get(id=id_bibliografia)  
    form = BibliografiaForm(instance=bibliografia)
    mensaje_exito = None
    mensaje_error = None
    
    if request.method == 'POST':
        form = BibliografiaForm(request.POST, instance=bibliografia)  
        if form.is_valid():
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                instance.save()
                mensaje_exito="Añadimos la bibliografía correctamente." 

                return redirect('planificaciones:bibliografia', id_planificacion=id_planificacion)

                 
            except:  
                 mensaje_error = "No pudimos añadir la bibliografía." 

        else:
            mensaje_error = "No pudimos añadir la bibliografía." 

    context = {
        'planificacion': planificacion,
        'bibliografia': bibliografia,
        "form": form,
        "mensaje_exito": mensaje_exito,
        "mensaje_error": mensaje_error,
    }

    return render(request,"secciones/bibliografia/update.html", context) 



def Deletebibliografia(request, id_planificacion, id_bibliografia):
    mensaje_exito = None
    mensaje_error = None

    if request.method == "POST":
        try:
            bibliografia = Bibliografia.objects.get(id=id_bibliografia)  
            bibliografia.delete()
            mensaje_exito = "Se ha borrado correctamente."        
        except:
            mensaje_error = "No pudimos borrar correctamente"  
        
        return redirect('planificaciones:bibliografia', id_planificacion=id_planificacion)