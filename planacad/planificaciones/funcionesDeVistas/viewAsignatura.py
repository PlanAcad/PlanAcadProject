from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Para usar los objetos y/o funciones de 'redirect'
from planificaciones.formularios.formPlanificacion import PlanificacionForm
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formAsignatura import AsignaturaForm 
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelCarrera import Carrera
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.formularios.formFechaCalendarioAcademico import FechaCalendarioAcademico
from datetime import datetime


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
    if "profesor" in  usergroup or "consejo" in  usergroup :
        asignaturas = Asignatura.objects.filter(profesor=request.user)
        calendario = FechaCalendarioAcademico.objects.filter(ciclo_lectivo=datetime.now().year).filter(nombre_mes=datetime.now().strftime("%B")).exclude(actividad='DN').order_by('fecha')
    elif "jefe de carrera" in  usergroup :
        carreraUsuario = request.user.carrera.all()
        print(carreraUsuario)
        if(carreraUsuario.count()==1):
            carrera = Carrera.objects.get(id = carreraUsuario.first().id) 
            asignaturas = Asignatura.objects.filter(carrera = carrera)
            calendario = FechaCalendarioAcademico.objects.filter(ciclo_lectivo=datetime.now().year).filter(nombre_mes=datetime.now().strftime("%B")).exclude(actividad='DN').order_by('fecha')
    elif "alumno" in usergroup: 
        asignaturas = Asignatura.objects.all()
        calendario = FechaCalendarioAcademico.objects.filter(ciclo_lectivo=datetime.now().year).filter(nombre_mes=datetime.now().strftime("%B")).exclude(actividad='DN').order_by('fecha')
    context = {
            'asignaturas': asignaturas.order_by('ano'),
            'calendario':calendario, 
        }  
    return render(request,'asignaturas/index.html', context)
    
def AsignaturaDetailView(request, id, error = 'False'):
    print(error)
    mostrar_error = error == 'True'  
    asignatura = Asignatura.objects.get(id=id)  
    # Obtengo el nombre de la carrera
    carrera = Carrera.objects.get(id=asignatura.carrera_id)
    # Obtener planificaciones existentes
    usergroup = request.user.groups.values_list('name',flat = True)
    if "profesor" in  usergroup  :
        planificaciones = Planificacion.objects.filter(asignatura=asignatura).filter(eliminada=False).order_by('fecha_creacion')
    elif "jefe de carrera" in  usergroup or "consejo" in  usergroup :
        planificaciones = Planificacion.objects.filter(asignatura=asignatura).filter(Q(estado = 'R') | Q(estado = 'A')).filter(eliminada=False).order_by('fecha_creacion')
    elif "alumno" in usergroup:
        planificaciones = Planificacion.objects.filter(Q(asignatura=asignatura) and Q(estado = 'A')).filter(eliminada=False).order_by('fecha_creacion')
    

    # Mandarle el form para crear planificaciones
    form = PlanificacionForm()  

    calendario = FechaCalendarioAcademico.objects.filter(ciclo_lectivo=datetime.now().year).filter(nombre_mes=datetime.now().strftime("%B")).exclude(actividad='DN').order_by('fecha')
    msgError = None
    if mostrar_error:
        msgError = "Ha ocurrido un error"
    context = {
            'planificaciones':planificaciones,
            'asignatura': asignatura,
            'carrera':carrera,
            'form':form, 
            'calendario': calendario,
            'error':msgError
        }
    return render(request,'asignaturas/detail.html',context)  

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

def AsignaturaDestroy(request, id):  
    asignatura = Asignatura.objects.get(id=id)  
    asignatura.delete()  
    return asignatura("/show") 

def PapeleraView(request, id_asignatura):  
    asignatura = Asignatura.objects.get(id=id_asignatura)  
    carrera = Carrera.objects.get(id=asignatura.carrera_id)
    planificaciones = Planificacion.objects.filter(asignatura=asignatura).filter(eliminada=True).order_by('id')
    context = {
            'planificaciones':planificaciones,
            'asignatura': asignatura,
            'carrera':carrera, 
        }  
    return render(request,'asignaturas/papelera.html', context)   