# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelContenido import Contenido
from planificaciones.formularios.formCorreccion import CorreccionForm


# To show and to add new one
def CorreccionNew(request, id_planificacion, id_seccion):   
    planificacion = Planificacion.objects.get(id=id_planificacion)
    if request.method == 'POST':
        form = CorreccionForm(request.POST)
        if form.is_valid():
            try:  
                instance = form.save(commit=False)  
                instance.planificacion_id=planificacion.id
                instance.seccion = id_seccion
                instance.estado = 'G'
                instance.save()
                mensaje_exito="Añadimos el contenido correctamente."   
            except:  
                mensaje_error = "No pudimos añadir el contenido." 
                print(form.errors)
        else:
            mensaje_error = "No pudimos añadir el contenido."  
            print(form.errors)
        if   id_seccion==1:
            return redirect('planificaciones:datosDescriptivos', id_planificacion=planificacion.id)
        elif id_seccion==2:
            return redirect('planificaciones:detallesprofesorcatedra', id_planificacion=planificacion.id)
        elif id_seccion==3:
            return redirect('planificaciones:fundamentacion', id_planificacion=planificacion.id)
        elif id_seccion==4:
            return redirect('planificaciones:resultadosDeAprendizajes', id_planificacion=planificacion.id)
        elif id_seccion==5:
            return redirect('planificaciones:competencias', id_planificacion=planificacion.id)
        elif id_seccion==6:
            return redirect('planificaciones:propuestaDesarrollo', id_planificacion=planificacion.id)
        elif id_seccion==7:
            return redirect('planificaciones:sistemaDeEvaluacion', id_planificacion=planificacion.id)
        elif id_seccion==71:
            return redirect('planificaciones:aprobacionDirecta', id_planificacion=planificacion.id)
        elif id_seccion==72:
            return redirect('planificaciones:aprobacionCursada', id_planificacion=planificacion.id)
        elif id_seccion==8:
            return redirect('planificaciones:cronograma', id_planificacion=planificacion.id)
        elif id_seccion==9:
            return redirect('planificaciones:bibliografia', id_planificacion=planificacion.id)
        elif id_seccion==10:
            return redirect('planificaciones:webgrafia', id_planificacion=planificacion.id)
        elif id_seccion==11:
            return redirect('planificaciones:contenido', id_planificacion=planificacion.id)
        elif id_seccion==12:
            return redirect('planificaciones:distribucionDeTareas', id_planificacion=planificacion.id)
        elif id_seccion==13:
            return redirect('planificaciones:justificacionOrdenanza', id_planificacion=planificacion.id)



# To show and to add new one
# def CorreccionUpdate(request, id_planificacion, id_contenido):   
#     planificacion = Planificacion.objects.get(id=id_planificacion) 
#     contenido = Contenido.objects.get(id=id_contenido)  
#     form = ContenidoForm(instance=contenido)
#     mensaje_exito = None
#     mensaje_error = None
    
#     if request.method == 'POST':
#         form = ContenidoForm(request.POST, instance=contenido)  
#         if form.is_valid():
#             try:  
#                 instance = form.save(commit=False)
#                 instance.planificacion_id=planificacion.id
#                 instance.save()
#                 mensaje_exito="Añadimos el contenido correctamente." 

#                 return redirect('planificaciones:contenido', id_planificacion=id_planificacion)

                 
#             except:  
#                 mensaje_error = "No pudimos añadir el contenido." 
#                 print(form.errors)


#         else:
#             mensaje_error = "No pudimos añadir el contenido." 
#             print(form.errors)


#     context = {
#         'planificacion': planificacion,
#         'contenido': contenido,
#         "form": form,
#         "mensaje_exito": mensaje_exito,
#         "mensaje_error": mensaje_error,
#     }

#     return render(request,"secciones/contenido/update.html", context) 

