# Para usar los objetos y/o funciones de 'redirect'
from django.db.models import fields
from django.shortcuts import render, redirect
from planificaciones.modelos.modelBibliografia import Bibliografia
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.formularios.formResultadoDeAprendizaje import ResultadoDeAprendizajeForm
from planificaciones.modelos.modelResultadoAprendizaje import ResultadoDeAprendizaje
from planificaciones.modelos.modelPropuestaDesarrollo import PropuestaDesarrollo
from planificaciones.formularios.formPropuestaDesarrollo import PropuestaDesarrolloForm
from planificaciones.modelos.modelSubCompetencia import SubCompetencia
from planificaciones.modelos.modelCompetencia import Competencia
from planificaciones.modelos.modelContenido import Contenido
from planificaciones.modelos.modelUnidad import Unidad
#Agregar
from django.db.models import Q
from planificaciones.modelos.modelCorrecciones import Correccion
#Correcciones
from planificaciones.formularios.formCorreccion import CorreccionForm
from planificaciones.funcionesDeVistas import viewCorreccion
#Comentarios
from planificaciones.formularios.formComentarios import ComentarioForm
from django.contrib.auth.decorators import login_required



# To show and to add new one
@login_required
def IndexPropuestaDesarrollo(request, id_planificacion):  
    # General 
    planificacion = Planificacion.objects.get(id=id_planificacion) 
    mensaje_exito = None
    mensaje_error = None 

    # PARA RESULTADOS DE APRENDIZAJE
    resultados_aprendizaje = ResultadoDeAprendizaje.objects.filter(planificacion=planificacion) 
    resultados_aprendizaje_materia = resultados_aprendizaje.filter(asignatura=planificacion.asignatura).order_by('id')

    # PARA PROPUESTAS DE DESARROLLO
    propuestas_desarrollo = PropuestaDesarrollo.objects.filter(planificacion=planificacion) 

    # Subcompetencias: Listar todas las subcompetencias que tienen asociadas las competencias asociadas a la planificación. Puede seleccionar multiples.
    competencias_planificacion = Competencia.objects.filter(planificacion=planificacion)
    subcompetencias_planificacion = SubCompetencia.objects.filter(competencia__in = competencias_planificacion)

    # Unidades: Las unidades sacar de Unidades
    unidades = Unidad.objects.filter(planificacion_id=planificacion.id)

    # Bibliografias: Listar todos las Bibliografias que estén asociadas a la planificación. Puede seleccionar multiples.
    bibliografias_planificacion = Bibliografia.objects.filter(planificacion=planificacion)
    
    #CORRECCIONES
    correcciones = Correccion.objects.filter(Q(planificacion_id = id_planificacion) & Q(seccion = 6)).prefetch_related('comentarios')
    correcciones = viewCorreccion.OrderCorrecciones(correcciones)
    correccionesEnSecciones = viewCorreccion.CorreccionesEnSecciones(id_planificacion)
    existen_correcciones_pendientes = None
    #Forms Correcciones y Comentarios
    correccionForm = CorreccionForm()
    comentarioForm = ComentarioForm()
    
    for item in correcciones:
        print(item.estado)
        if(item.estado == "G"):
            existen_correcciones_pendientes = "Existen observaciones pendientes de resolver"

    if request.method == 'POST':
        if request.POST.get("form_name") == "resultado_aprendizaje":
            form_resultado_aprendizaje = ResultadoDeAprendizajeForm(request.POST)
            if form_resultado_aprendizaje.is_valid():
                try:  
                    instance = form_resultado_aprendizaje.save(commit=False)
                    instance.planificacion_id=planificacion.id
                    instance.asignatura=planificacion.asignatura
                    instance.save()
                        
                    mensaje_exito="Añadimos el resultado de aprendizaje correctamente."  
                    
                except:  
                    mensaje_error = "No pudimos añadir el resultado de aprendizaje." 
                    print(form_resultado_aprendizaje.errors)

            else:
                mensaje_error = "No pudimos añadir el resultado de aprendizaje." 
                print(form_resultado_aprendizaje.errors)
        
        if request.POST.get("form_name") == "propuesta_desarollo":
            form_propuesta_desarrollo = PropuestaDesarrolloForm(request.POST)
            if form_propuesta_desarrollo.is_valid():
                try:  
                    instance = form_propuesta_desarrollo.save(commit=False)
                    instance.planificacion_id=planificacion.id
                    instance.save()
                    form_propuesta_desarrollo.save_m2m()  
                    mensaje_exito="Añadimos la propuesta de desarrollo correctamente."  
                    
                except:  
                    mensaje_error = "No pudimos añadir la propuesta de desarrollo correctamente." 
                    print(form_propuesta_desarrollo.errors)

            else:
                mensaje_error = "No pudimos añadir la propuesta de desarrollo correctamente." 
                print(form_propuesta_desarrollo.errors)

    form_resultado_aprendizaje = ResultadoDeAprendizajeForm()
    form_propuesta_desarrollo = PropuestaDesarrolloForm()
    form_propuesta_desarrollo.fields['subcompetencias'].queryset = subcompetencias_planificacion
    form_propuesta_desarrollo.fields['resultados_de_aprendizaje'].queryset = resultados_aprendizaje_materia
    form_propuesta_desarrollo.fields['unidades'].queryset = unidades
    form_propuesta_desarrollo.fields['bibliografias'].queryset = bibliografias_planificacion

    context = {
        'planificacion': planificacion,
        'resultados_aprendizaje_materia': resultados_aprendizaje_materia,
        "form_resultado_aprendizaje": form_resultado_aprendizaje,
        "propuestas_desarrollo": propuestas_desarrollo,
        "form_propuesta_desarrollo": form_propuesta_desarrollo,
        "unidades_planificacion": unidades,
        "bibliografias_planificacion": bibliografias_planificacion,
        'correcciones':correcciones,
        #Forms Correcciones
        'correccion_form': correccionForm,
        'comentario_form':comentarioForm,
        'correccionesEnSecciones':correccionesEnSecciones,
        #
        'existen_correcciones_pendientes':existen_correcciones_pendientes,
        "mensaje_exito": mensaje_exito,
        "mensaje_error": mensaje_error,
    }

    return render(request,"secciones/propuesta-desarrollo/index.html", context) 

@login_required
def UpdateResultadoAprendizaje(request, id_planificacion, id_resultado_aprendizaje):   
    planificacion = Planificacion.objects.get(id=id_planificacion) 
    resultado_aprendizaje = ResultadoDeAprendizaje.objects.get(id=id_resultado_aprendizaje)  
    form = ResultadoDeAprendizajeForm(instance=resultado_aprendizaje)
    mensaje_exito = None
    mensaje_error = None
    
    if request.method == 'POST':
        form = ResultadoDeAprendizajeForm(request.POST, instance=resultado_aprendizaje)  
        if form.is_valid():
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                instance.asignatura=planificacion.asignatura
                instance.save()
                mensaje_exito="Actualizamos el resultado de aprendizaje correctamente." 

                return redirect('planificaciones:propuestaDesarrollo', id_planificacion=id_planificacion)

                 
            except:  
                mensaje_error = "No pudimos actualizar el resultado de aprendizaje." 
                print(form.errors)


        else:
            mensaje_error = "No pudimos añadir el resultado de aprendizaje." 
            print(form.errors)

    correcciones = Correccion.objects.filter(Q(planificacion_id = id_planificacion) & Q(seccion = 6)).prefetch_related('comentarios')
    correcciones = viewCorreccion.OrderCorrecciones(correcciones)
    correccionesEnSecciones = viewCorreccion.CorreccionesEnSecciones(id_planificacion)
    context = {
        'planificacion': planificacion,
        'resultado_aprendizaje': resultado_aprendizaje,
        "form": form,
        'correccionesEnSecciones':correccionesEnSecciones,
        "mensaje_exito": mensaje_exito,
        "mensaje_error": mensaje_error,
    }

    return render(request,"secciones/propuesta-desarrollo/update-resultado-aprendizaje.html", context) 

@login_required
def DeleteResultadoAprendizaje(request, id_planificacion, id_resultado_aprendizaje):
    if request.method == "POST":
        try:
            resultado_aprendizaje = ResultadoDeAprendizaje.objects.get(id=id_resultado_aprendizaje)  
            resultado_aprendizaje.delete()
            mensaje_exito = "Se ha borrado correctamente."  

        except:
            mensaje_error = "No pudimos borrar correctamente"  
        
        return redirect('planificaciones:propuestaDesarrollo', id_planificacion=id_planificacion)

@login_required
def UpdatePropuestaDesarrollo(request, id_planificacion, id_propuesta_desarrollo):   
    # General 
    planificacion = Planificacion.objects.get(id=id_planificacion) 
    propuesta_desarrollo = PropuestaDesarrollo.objects.get(id=id_propuesta_desarrollo)  
    form_propuesta_desarrollo = PropuestaDesarrolloForm(instance=propuesta_desarrollo)
    mensaje_exito = None
    mensaje_error = None
    
    # PARA RESULTADOS DE APRENDIZAJE
    resultados_aprendizaje = ResultadoDeAprendizaje.objects.filter(planificacion=planificacion) 
    resultados_aprendizaje_materia = resultados_aprendizaje.filter(asignatura=planificacion.asignatura).order_by('id')

    # PARA PROPUESTAS DE DESARROLLO
    propuestas_desarrollo = PropuestaDesarrollo.objects.filter(planificacion=planificacion) 

    # Subcompetencias: Listar todas las subcompetencias que tienen asociadas las competencias asociadas a la planificación. Puede seleccionar multiples.
    competencias_planificacion = Competencia.objects.filter(planificacion=planificacion)
    subcompetencias_planificacion = SubCompetencia.objects.filter(competencia__in = competencias_planificacion)

    # Unidades: Las unidades sacar de Unidades
    unidades = Unidad.objects.filter(planificacion_id=planificacion.id)

    # Bibliografias: Listar todos las Bibliografias que estén asociadas a la planificación. Puede seleccionar multiples.
    bibliografias_planificacion = Bibliografia.objects.filter(planificacion=planificacion)
    
    form_propuesta_desarrollo.fields['subcompetencias'].queryset = subcompetencias_planificacion
    form_propuesta_desarrollo.fields['resultados_de_aprendizaje'].queryset = resultados_aprendizaje_materia
    form_propuesta_desarrollo.fields['unidades'].queryset = unidades
    form_propuesta_desarrollo.fields['bibliografias'].queryset = bibliografias_planificacion

    
    if request.method == 'POST':
        form_propuesta_desarrollo = PropuestaDesarrolloForm(request.POST, instance=propuesta_desarrollo)  
        if form_propuesta_desarrollo.is_valid():
            try:  
                instance = form_propuesta_desarrollo.save(commit=False)
                instance.planificacion_id=planificacion.id
                instance.save()
                form_propuesta_desarrollo.save_m2m()  
                mensaje_exito="Actualizamos la propuesta de desarrollo correctamente." 
                return redirect('planificaciones:propuestaDesarrollo', id_planificacion=id_planificacion)

                 
            except:  
                mensaje_error = "No pudimos actualizar la propuesta de desarrollo." 
                print(form_propuesta_desarrollo.errors)


        else:
            mensaje_error = "No pudimos actualizar la propuesta de desarrollo." 
            print(form_propuesta_desarrollo.errors)

    correccionesEnSecciones = viewCorreccion.CorreccionesEnSecciones(id_planificacion)
    context = {
        'planificacion': planificacion,
        'resultados_aprendizaje_materia': resultados_aprendizaje_materia,
        "propuesta_desarrollo": propuesta_desarrollo,
        "form": form_propuesta_desarrollo,
        "subcompetencias_planificacion": subcompetencias_planificacion,
        "unidades_planificacion": unidades,
        "bibliografias_planificacion": bibliografias_planificacion,
        'correccionesEnSecciones':correccionesEnSecciones,
        "mensaje_exito": mensaje_exito,
        "mensaje_error": mensaje_error,
    }

    return render(request,"secciones/propuesta-desarrollo/update-propuesta-desarrollo.html", context) 

@login_required
def DeletePropuestaDesarrollo(request, id_planificacion, id_propuesta_desarrollo):
    if request.method == "POST":
        try:
            propuesta_desarrollo = PropuestaDesarrollo.objects.get(id=id_propuesta_desarrollo)  
            propuesta_desarrollo.delete()
            mensaje_exito = "Se ha borrado correctamente."  
                  
        except:
            mensaje_error = "No pudimos borrar correctamente"  
        
        return redirect('planificaciones:propuestaDesarrollo', id_planificacion=id_planificacion)