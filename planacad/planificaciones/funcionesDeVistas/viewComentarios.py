# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect
from planificaciones.modelos.modelCorrecciones import Correccion
from planificaciones.modelos.modelComentarios import Comentario
from planificaciones.formularios.formComentarios import ComentarioForm


# To to add new one
def ComentarioNew(request, id_correccion, id_seccion):
    correccion = Correccion.objects.get(id=id_correccion)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            try:  
                instance = form.save(commit=False)  
                instance.correccion_id=correccion.id
                instance.save()
                mensaje_exito="Añadimos el contenido correctamente."  
            except:  
                mensaje_error = "No pudimos añadir el contenido."
                print(form.errors)
        else:
            mensaje_error = "No pudimos añadir el contenido."  
            print(form.errors)
        if   id_seccion==1:
            return redirect('planificaciones:datosDescriptivos', id_planificacion=correccion.planificacion.id)
        elif id_seccion==2:
            return redirect('planificaciones:detallesprofesorcatedra', id_planificacion=correccion.planificacion.id)
        elif id_seccion==3:
            return redirect('planificaciones:fundamentacion', id_planificacion=correccion.planificacion.id)
        elif id_seccion==4:
            return redirect('planificaciones:resultadosDeAprendizajes', id_planificacion=correccion.planificacion.id)
        elif id_seccion==5:
            return redirect('planificaciones:competencias', id_planificacion=correccion.planificacion.id)
        elif id_seccion==6:
            return redirect('planificaciones:propuestaDesarrollo', id_planificacion=correccion.planificacion.id)
        elif id_seccion==7:
            return redirect('planificaciones:sistemaDeEvaluacion', id_planificacion=correccion.planificacion.id)
        elif id_seccion==71:
            return redirect('planificaciones:aprobacionDirecta', id_planificacion=correccion.planificacion.id)
        elif id_seccion==72:
            return redirect('planificaciones:aprobacionCursada', id_planificacion=correccion.planificacion.id)
        elif id_seccion==8:
            return redirect('planificaciones:cronograma', id_planificacion=correccion.planificacion.id)
        elif id_seccion==9:
            return redirect('planificaciones:bibliografia', id_planificacion=correccion.planificacion.id)
        elif id_seccion==10:
            return redirect('planificaciones:webgrafia', id_planificacion=correccion.planificacion.id)
        elif id_seccion==11:
            return redirect('planificaciones:contenido', id_planificacion=correccion.planificacion.id)
        elif id_seccion==12:
            return redirect('planificaciones:distribucionDeTareas', id_planificacion=correccion.planificacion.id)
        elif id_seccion==13:
            return redirect('planificaciones:justificacionOrdenanza', id_planificacion=correccion.planificacion.id)

