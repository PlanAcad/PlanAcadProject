from django.db.models import Q
# Para usar los objetos y/o funciones de 'redirect'
from planificaciones.formularios.formPlanificacion import PlanificacionForm
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formAsignatura import AsignaturaForm 
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelCarrera import Carrera
from planificaciones.modelos.modelClase import Clase
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelUsuarioPlanificacion import PlanificacionUsuario

from planificaciones.formularios.formFechaCalendarioAcademico import FechaCalendarioAcademico
from planificaciones.funcionesDeVistas import viewCalendario
from datetime import datetime
from django.contrib.auth.decorators import login_required

@login_required
def AsignaturaNew(request):
    form = AsignaturaForm()
    if request.method == "POST":
        form = AsignaturaForm(request.POST)  
        if form.is_valid():
            print("guarda")
            asig = form.save(commit=False)
            asig.save()
            form.save_m2m()
            return redirect('planificaciones:asignaturas')
    context = {
        'form':form, 
    }      
    return render(request, 'asignaturas/add.html', context)

@login_required
def AsignaturasView(request):
    # Obtener materias del profesor
    asignaturas = None
    calendario = None
    usergroup = request.user.groups.values_list('name',flat = True)

    usuariosPlanificacion = PlanificacionUsuario.objects.filter(usuario_id = request.user.id)
    fechasParciales = None

    if "profesor" in  usergroup or "consejo" in  usergroup :
        asignaturas = Asignatura.objects.filter(profesor=request.user)
        asignaturasProfesor = Asignatura.objects.filter(profesor = request.user)
        for asig in asignaturasProfesor:
            planificacion = Planificacion.objects.get(asignatura = asig)
            if(planificacion.datos_descriptivos.ciclo_lectivo == datetime.now().year & planificacion.estado == 'A'):
                fechasParciales = Clase.objects.filter(planificacion = planificacion).filter(Q(es_examen = 'R') | Q(es_examen = 'A')).filter(fecha_clase__month =datetime.now().month)
    elif "jefe de carrera" in  usergroup :
        carreraUsuario = request.user.carrera.all()
        if(carreraUsuario.count()==1):
            carrera = Carrera.objects.get(id = carreraUsuario.first().id) 
            asignaturas = Asignatura.objects.filter(carrera = carrera)
        for asig in asignaturasProfesor:
            planificacion = Planificacion.objects.get(asignatura = asig)
            if(planificacion.datos_descriptivos.ciclo_lectivo == datetime.now().year & planificacion.estado == 'A'):
                fechasParciales = Clase.objects.filter(planificacion = planificacion).filter(Q(es_examen = 'R') | Q(es_examen = 'A')).filter(fecha_clase__month =datetime.now().month)
    
    elif "alumno" in usergroup:
        carreraUsuario = request.user.carrera.all()
        if(carreraUsuario.count()==1):
            carrera = Carrera.objects.get(Q(id = carreraUsuario.first().id) | Q(nombre_carrera = "Basicas") ) 
            asignaturas = Asignatura.objects.filter(carrera = carrera) 
        for up in usuariosPlanificacion:
            planificacion = Planificacion.objects.get(id = up.planificacion_id)
            if(planificacion.datos_descriptivos.ciclo_lectivo == datetime.now().year & planificacion.estado == 'A'):
                fechasParciales = Clase.objects.filter(planificacion = planificacion).filter(Q(es_examen = 'R') | Q(es_examen = 'A')).filter(fecha_clase__month =datetime.now().month)

      
    calendarioAcademico = FechaCalendarioAcademico.objects.filter(ciclo_lectivo=datetime.now().year).filter(nombre_mes=datetime.now().strftime("%B")).exclude(actividad='DN').order_by('fecha')    
    
    calendario = viewCalendario.CreateCalendario(calendarioAcademico, fechasParciales)

    context = {
            'asignaturas': asignaturas.order_by('ano'),
            'calendario':calendario, 
        }  
    return render(request,'asignaturas/index.html', context)

@login_required
def AsignaturaDetailView(request, id, error = 'False'):
    print(error)
    mostrar_error = error == 'True'  
    asignatura = Asignatura.objects.get(id=id)  
    # Obtengo el nombre de la carrera
    carrera = Carrera.objects.get(id=asignatura.carrera_id)
    # Obtener planificaciones existentes
    usergroup = request.user.groups.values_list('name',flat = True)
    planificacionesDeAsignatura = Planificacion.objects.filter(asignatura=asignatura).filter(eliminada=False).exists()
    usuariosPlanificacion = PlanificacionUsuario.objects.filter(usuario_id = request.user.id)
    fechasParciales = None
    if "profesor" in  usergroup  :
        planificaciones = Planificacion.objects.filter(asignatura=asignatura).filter(eliminada=False).order_by('fecha_creacion')
        asignaturasProfesor = Asignatura.objects.filter(profesor = request.user)
        for asig in asignaturasProfesor:
            planificacion = Planificacion.objects.get(asignatura = asig)
            if(planificacion.datos_descriptivos.ciclo_lectivo == datetime.now().year & planificacion.estado == 'A'):
                fechasParciales = Clase.objects.filter(planificacion = planificacion).filter(Q(es_examen = 'R') | Q(es_examen = 'A')).filter(fecha_clase__month =datetime.now().month)
    elif "jefe de carrera" in  usergroup or "consejo" in  usergroup :
        planificaciones = Planificacion.objects.filter(asignatura=asignatura).filter(Q(estado = 'R') | Q(estado = 'A')).filter(eliminada=False).order_by('fecha_creacion')
        asignaturasProfesor = Asignatura.objects.filter(profesor = request.user)
        for asig in asignaturasProfesor:
            planificacion = Planificacion.objects.get(asignatura = asig)
            if(planificacion.datos_descriptivos.ciclo_lectivo == datetime.now().year & planificacion.estado == 'A'):
                fechasParciales = Clase.objects.filter(planificacion = planificacion).filter(Q(es_examen = 'R') | Q(es_examen = 'A')).filter(fecha_clase__month =datetime.now().month)
    elif "alumno" in usergroup:
        planificaciones = Planificacion.objects.filter(asignatura=asignatura).filter(estado = 'A').filter(eliminada=False).order_by('fecha_creacion')
        for up in usuariosPlanificacion:
            planificacion = Planificacion.objects.get(id = up.planificacion_id)
            if(planificacion.datos_descriptivos.ciclo_lectivo == datetime.now().year & planificacion.estado == 'A'):
                fechasParciales = Clase.objects.filter(planificacion = planificacion).filter(Q(es_examen = 'R') | Q(es_examen = 'A')).filter(fecha_clase__month =datetime.now().month)


    # Mandarle el form para crear planificaciones
    form = PlanificacionForm()  

    calendarioAcademico = FechaCalendarioAcademico.objects.filter(ciclo_lectivo=datetime.now().year).filter(nombre_mes=datetime.now().strftime("%B")).exclude(actividad='DN').order_by('fecha')    
    
    calendario = viewCalendario.CreateCalendario(calendarioAcademico, fechasParciales)

    msgError = None
    if mostrar_error:
        msgError = "La planificacion tiene un problema y no es posible tomarla como referencia"
    context = {
            'planificaciones':planificaciones,
            'planificacionesDeAsignatura':planificacionesDeAsignatura,
            'asignatura': asignatura,
            'carrera':carrera,
            'form':form, 
            'usuariosPlanificacion':usuariosPlanificacion,
            'calendario': calendario,
            'error':msgError
        }
    return render(request,'asignaturas/detail.html',context)  

@login_required
def AsignaturaUpdate(request, id):  
    asignatura = Asignatura.objects.get(id=id)
    form = AsignaturaForm(instance = asignatura)
    if request.method == "POST":  
        form = AsignaturaForm(request.POST, instance = asignatura)  
        if form.is_valid():
            asig = form.save(commit=False)
            asig.save()
            form.save_m2m()
            return redirect('planificaciones:asignaturas')
    context = {
        'asignatura': asignatura,
        'form':form, 
    }      
    return render(request, 'asignaturas/update.html', context)  

@login_required
def AsignaturaDestroy(request, id):  
    asignatura = Asignatura.objects.get(id=id)  
    asignatura.delete()  
    return asignatura("/show") 

@login_required
def PapeleraView(request, id_asignatura):  
    asignatura = Asignatura.objects.get(id=id_asignatura)  
    carrera = Carrera.objects.get(id=asignatura.carrera_id)
    planificaciones = Planificacion.objects.filter(asignatura=asignatura).filter(eliminada=True).order_by('fecha_creacion')
    context = {
            'planificaciones':planificaciones,
            'asignatura': asignatura,
            'carrera':carrera, 
        }  
    return render(request,'asignaturas/papelera.html', context)   