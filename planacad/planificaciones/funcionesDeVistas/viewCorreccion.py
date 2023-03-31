# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelCorrecciones import Correccion
from planificaciones.formularios.formCorreccion import CorreccionForm
from django.contrib.auth.decorators import login_required



# To to add new one
@login_required
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
            return redirect('planificaciones:sistemaDeEvaluacion', planificacion_id=planificacion.id)
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


# To to add new one
@login_required
def CorreccionUpdate(request, id_correccion):
    data = Correccion.objects.get(id = id_correccion)
    if request.method == 'POST':
        data.estado = 'R'
        data.save(update_fields=["estado"]) 
    
        if   data.seccion ==1:
            return redirect('planificaciones:datosDescriptivos', id_planificacion=data.planificacion.id)
        elif data.seccion ==2:
            return redirect('planificaciones:detallesprofesorcatedra', id_planificacion=data.planificacion.id)
        elif data.seccion ==3:
            return redirect('planificaciones:fundamentacion', id_planificacion=data.planificacion.id)
        elif data.seccion ==4:
            return redirect('planificaciones:resultadosDeAprendizajes', id_planificacion=data.planificacion.id)
        elif data.seccion ==5:
            return redirect('planificaciones:competencias', id_planificacion=data.planificacion.id)
        elif data.seccion ==6:
            return redirect('planificaciones:propuestaDesarrollo', id_planificacion=data.planificacion.id)
        elif data.seccion ==7:
            return redirect('planificaciones:sistemaDeEvaluacion', planificacion_id=data.planificacion.id)
        elif data.seccion ==71:
            return redirect('planificaciones:aprobacionDirecta', id_planificacion=data.planificacion.id)
        elif data.seccion ==72:
            return redirect('planificaciones:aprobacionCursada', id_planificacion=data.planificacion.id)
        elif data.seccion ==8:
            return redirect('planificaciones:cronograma', id_planificacion=data.planificacion.id)
        elif data.seccion ==9:
            return redirect('planificaciones:bibliografia', id_planificacion=data.planificacion.id)
        elif data.seccion ==10:
            return redirect('planificaciones:webgrafia', id_planificacion=data.planificacion.id)
        elif data.seccion ==11:
            return redirect('planificaciones:contenido', id_planificacion=data.planificacion.id)
        elif data.seccion ==12:
            return redirect('planificaciones:distribucionDeTareas', id_planificacion=data.planificacion.id)
        elif data.seccion ==13:
            return redirect('planificaciones:justificacionOrdenanza', id_planificacion=data.planificacion.id)



# To to add new one
def CorreccionesEnSecciones(id_planificacion):
    correccionesEnSecciones = []
    correcciones = Correccion.objects.filter(planificacion_id = id_planificacion).filter(estado = "G")
    if(correcciones.filter(seccion = 1).exists()):
        correccionesEnSecciones.append("1")
    if(correcciones.filter(seccion = 2).exists()):
        correccionesEnSecciones.append("2")
    if(correcciones.filter(seccion = 3).exists()):
        correccionesEnSecciones.append("3")
    if(correcciones.filter(seccion = 4).exists()):
        correccionesEnSecciones.append("4")
    if(correcciones.filter(seccion = 5).exists()):
        correccionesEnSecciones.append("5")
    if(correcciones.filter(seccion = 6).exists()):
        correccionesEnSecciones.append("6")
    if(correcciones.filter(seccion = 7).exists()):
        correccionesEnSecciones.append("7")
    if(correcciones.filter(seccion = 71).exists()):
        correccionesEnSecciones.append("7.1")
    if(correcciones.filter(seccion = 72).exists()):
        correccionesEnSecciones.append("7.2")
    if(correcciones.filter(seccion = 8).exists()):
        correccionesEnSecciones.append("8")
    if(correcciones.filter(seccion = 9).exists()):
        correccionesEnSecciones.append("9")
    if(correcciones.filter(seccion = 10).exists()):
        correccionesEnSecciones.append("10")
    if(correcciones.filter(seccion = 11).exists()):
        correccionesEnSecciones.append("11")
    if(correcciones.filter(seccion = 12).exists()):
        correccionesEnSecciones.append("12")
    if(correcciones.filter(seccion = 13).exists()):
        correccionesEnSecciones.append("13")
    return correccionesEnSecciones
        
