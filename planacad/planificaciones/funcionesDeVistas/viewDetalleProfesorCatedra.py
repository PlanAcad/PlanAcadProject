# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
from django.urls import reverse

from django.http import HttpResponseRedirect
## import model and form
from planificaciones.formularios.formDetalleProfesorCatedra import DetalleProfesorCatedraForm
from planificaciones.formularios.formTareasFunciones import TareasFuncionesForm
from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra
from planificaciones.modelos.modelTareasFunciones import TareasFunciones
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelCategoria import Categoria
from planificaciones.modelos.modelSituacion import Situacion
from planificaciones.modelos.modelDedicacion import Dedicacion

#Agregar
from django.db.models import Q
from planificaciones.modelos.modelCorrecciones import Correccion
#Correcciones
from planificaciones.formularios.formCorreccion import CorreccionForm
from planificaciones.funcionesDeVistas import viewCorreccion
#Comentarios
from planificaciones.formularios.formComentarios import ComentarioForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, Group 
from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelTareasFunciones import TareasFunciones

import pandas as pd



##Define request for Asignatura   
@login_required
def DetalleProfesorCatedraNew(request, id_planificacion):
    mensaje_exito=None
    mensaje_error=None
    
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = DetalleProfesorCatedra.objects.filter(planificacion = planificacion)
    tareasFuncionesForm = TareasFuncionesForm()
    #CORRECCIONES
    correcciones = Correccion.objects.filter(Q(planificacion_id = id_planificacion) & Q(seccion = 2)).prefetch_related('comentarios')
    correccionesEnSecciones = viewCorreccion.CorreccionesEnSecciones(id_planificacion)
    existen_correcciones_pendientes = None
    #Forms Correcciones y Comentarios
    correccionForm = CorreccionForm()
    comentarioForm = ComentarioForm()
    
    for item in correcciones:
        if(item.estado == "G"):
            existen_correcciones_pendientes = "Existen correcciones pendientes de resolver"

    if request.method == "POST":  
        form = DetalleProfesorCatedraForm(request.POST)  
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                #Guardo
                instance.save()
                form.save_m2m()                    
                mensaje_exito="Añadimos el docente correctamente."  
            except:  
                 mensaje_error = "No pudimos añadir el docente."    
    
    form = DetalleProfesorCatedraForm()
    asignatura = Asignatura.objects.get(id= planificacion.asignatura.id)
    form.fields['profesor'].queryset = User.objects.filter(groups = Group.objects.get(name='profesor')).intersection(asignatura.profesor.all())
    
    form.fields['tareas'].queryset = TareasFunciones.objects.filter(planificacion_id = planificacion.id)
    #Agregar
    context = {
        'planificacion': planificacion,
        'data': data,
        'form':form,
        'tareasFuncionesForm':tareasFuncionesForm,
        'correcciones':correcciones,
        #Forms Correcciones
        'correccion_form': correccionForm,
        'comentario_form':comentarioForm,
        'correccionesEnSecciones':correccionesEnSecciones,
        #
        'existen_correcciones_pendientes':existen_correcciones_pendientes,
        'mensaje_exito': mensaje_exito, 
        'mensaje_error': mensaje_error
    }  
    return render(request,'secciones/detalles-profesor-catedra.html', context) 
  

@login_required
def ImportDetalleProfesorCatedra(request, id_planificacion):
    if request.method == 'POST':
        planificacion = Planificacion.objects.get(id=id_planificacion)
        # Leer el archivo Excel y convertirlo en un DataFrame
        df = pd.read_excel(request.FILES['excel_file'],engine='openpyxl')
        # Iterar sobre cada fila del DataFrame y crear usuarios de Django
        for _, row in df.iterrows():
            legajo = row['legajoProfesor']
            if not pd.isna(legajo):
                detalleProfesorCatedra = DetalleProfesorCatedra()
                categoria = Categoria.objects.get(categoria= row['categoria'])
                situacion = Situacion.objects.get(situacion= row['situacion'])
                dedicacion = Dedicacion.objects.get(dedicacion= row['dedicacion'])
                profesor = User.objects.get(username = legajo)

                detalleProfesorCatedra.planificacion = planificacion
                detalleProfesorCatedra.categoria = categoria
                detalleProfesorCatedra.situacion = situacion
                detalleProfesorCatedra.dedicacion = dedicacion
                detalleProfesorCatedra.profesor = profesor
                detalleProfesorCatedra.save()

        
        return redirect(reverse('planificaciones:detallesprofesorcatedra', args=[planificacion.id]) )


@login_required
def ProfesoresPorSituacion(request):
    planificacion_id = request.GET.get('planificacion')
    planificacion = Planificacion.objects.get(id=planificacion_id)
    situacion=request.GET.get('situacion')
    if(situacion == "2"):
        asignatura = Asignatura.objects.get(id= planificacion.asignatura.id)
        users = User.objects.filter(Q(groups = Group.objects.get(name='profesor')) | Q(groups = Group.objects.get(name='jefe de carrera'))).intersection(asignatura.profesor.all())
    elif(situacion == "3"):
        asignatura = Asignatura.objects.get(id= planificacion.asignatura.id)
        users = User.objects.filter(Q(groups = Group.objects.get(name='profesor'))| Q(groups = Group.objects.get(name='jefe de carrera'))).intersection(asignatura.profesor.all())
        users = User.objects.filter(Q(groups = Group.objects.get(name='alumno')) | Q(groups = Group.objects.get(name='consejo'))).union(users)
        
    return render(request, 'secciones/detalle-profesor-catedra-dropdown.html', {'users': users})


@login_required
def DetalleProfesorCatedraUpdate(request, id_planificacion, id_detalleprofesorcatedra):  
    mensaje_exito = None
    mensaje_error = None
    planificacion = Planificacion.objects.get(id=id_planificacion)
    data = DetalleProfesorCatedra.objects.get(id=id_detalleprofesorcatedra)
    if request.method == "POST":  
        form = DetalleProfesorCatedraForm(request.POST, instance=data)  
        if form.is_valid():  
            try:  
                instance = form.save(commit=False)
                instance.planificacion_id=planificacion.id
                #Guardo
                instance.save()
                form.save_m2m()
                mensaje_exito="Guardamos los cambios correctamente."
                return redirect('planificaciones:detallesprofesorcatedra', id_planificacion=id_planificacion)
                 
            except:  
                 mensaje_error = "No pudimos guardar los cambios."    
    else:  
        form = DetalleProfesorCatedraForm(instance=data)
        if(data.situacion == "2"):
            asignatura = Asignatura.objects.get(id= planificacion.asignatura.id)
            form.fields['profesor'].queryset = User.objects.filter(groups = Group.objects.get(name='profesor')).intersection(asignatura.profesor.all())
        elif(data.situacion == "3"):
            form.fields['profesor'].queryset = User.objects.filter(groups = Group.objects.get(name='alumno'))
        form.fields['tareas'].queryset = TareasFunciones.objects.filter(planificacion_id = planificacion.id)
        correccionesEnSecciones = viewCorreccion.CorreccionesEnSecciones(id_planificacion)

    return render(request,'secciones/detalles-profesor-catedra-update.html',{'data':data,'planificacion':planificacion,'form':form,'correccionesEnSecciones':correccionesEnSecciones, 'mensaje_error': mensaje_error,'mensaje_exito':mensaje_exito}) 
  
    
@login_required
def DetalleProfesorCatedraDestroy(request, id_planificacion, id_detalleprofesorcatedra):
    mensaje_exito = None
    mensaje_error = None
    if request.method == "POST":
        try:
            detalleProfesorCatedra = DetalleProfesorCatedra.objects.get(id=id_detalleprofesorcatedra)  
            detalleProfesorCatedra.delete()
            mensaje_exito = "Se ha borrado correctamente."        
        except:
            mensaje_error = "No pudimos borrar correctamente"  
        
        return redirect('planificaciones:detallesprofesorcatedra', id_planificacion=id_planificacion)
                 