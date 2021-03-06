# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelWebgrafia import Webgrafia
from planificaciones.formularios.formWebgrafia import WebgrafiaForm


# To show and to add new one
def IndexWebgrafia(request, id_planificacion):   
    planificacion = Planificacion.objects.get(id=id_planificacion)  
    webgrafias = Webgrafia.objects.filter(planificacion=planificacion)  
    mensaje_exito = None
    mensaje_error = None
    
    form = WebgrafiaForm()
    if request.method == 'POST':
        form = WebgrafiaForm(request.POST)
        if form.is_valid():
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                instance.save()
                    
                mensaje_exito="Añadimos la webgrafía correctamente."  
                 
            except:  
                mensaje_error = "No pudimos añadir la webgrafía." 
                print(form.errors)


        else:
            mensaje_error = "No pudimos añadir la webgrafía." 
            print(form.errors)


    context = {
        'planificacion': planificacion,
        'webgrafias': webgrafias,
        "form": form,
        "mensaje_exito": mensaje_exito,
        "mensaje_error": mensaje_error,
    }

    return render(request,"secciones/webgrafia/index.html", context) 



# To show and to add new one
def UpdateWebgrafia(request, id_planificacion, id_webgrafia):   
    planificacion = Planificacion.objects.get(id=id_planificacion) 
    webgrafia = Webgrafia.objects.get(id=id_webgrafia)  
    form = WebgrafiaForm(instance=webgrafia)
    mensaje_exito = None
    mensaje_error = None
    
    if request.method == 'POST':
        form = WebgrafiaForm(request.POST, instance=webgrafia)  
        if form.is_valid():
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                instance.save()
                mensaje_exito="Añadimos la webgrafía correctamente." 

                return redirect('planificaciones:webgrafia', id_planificacion=id_planificacion)

                 
            except:  
                mensaje_error = "No pudimos añadir la webgrafía." 
                print(form.errors)


        else:
            mensaje_error = "No pudimos añadir la webgrafía." 
            print(form.errors)


    context = {
        'planificacion': planificacion,
        'webgrafia': webgrafia,
        "form": form,
        "mensaje_exito": mensaje_exito,
        "mensaje_error": mensaje_error,
    }

    return render(request,"secciones/webgrafia/update.html", context) 



def DeleteWebgrafia(request, id_planificacion, id_webgrafia):
    mensaje_exito = None
    mensaje_error = None

    if request.method == "POST":
        try:
            webgrafia = Webgrafia.objects.get(id=id_webgrafia)  
            webgrafia.delete()
            mensaje_exito = "Se ha borrado correctamente."        
        except:
            mensaje_error = "No pudimos borrar correctamente"  
        
        return redirect('planificaciones:webgrafia', id_planificacion=id_planificacion)