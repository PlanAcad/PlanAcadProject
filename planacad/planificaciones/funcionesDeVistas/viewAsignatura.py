
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



##Define request for Asignatura   
def AsignaturaNew(request):  
    if request.method == "POST":  
        form = AsignaturaForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass  
    return render(request,'index.html') 

def AsignaturasView(request):  
    asignaturas = Asignatura.objects.all()  
    return render(request,"asignaturas/index.html",{'asignaturas':asignaturas})  
    
def AsignaturaDetailView(request, id):  
    asignatura = Asignatura.objects.get(id=id)  
    # Obtengo el nombre de la carrera
    carrera = Carrera.objects.get(id=asignatura.carrera_id)
    # Obtener planificaciones existentes
    planificaciones = Planificacion.objects.filter(asignatura=asignatura).filter(eliminada=False).order_by('id')
    # Mandarle el form para crear planificaciones
    form = PlanificacionForm()  

    calendario = FechaCalendarioAcademico.objects.filter(ciclo_lectivo=datetime.now().year).filter(nombre_mes=datetime.now().strftime("%B")).exclude(actividad='DN').order_by('fecha')

    return render(request,'asignaturas/detail.html', {'asignatura':asignatura, 'carrera':carrera, 'planificaciones':planificaciones, 'form':form, 'calendario': calendario})  
 
def AsignaturaUpdate(request, id):  
    asignatura = Asignatura.objects.get(id=id)  
    form = AsignaturaForm(request.POST, instance = asignatura)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'asignatura': asignatura})  

def AsignaturaDestroy(request, id):  
    asignatura = Asignatura.objects.get(id=id)  
    asignatura.delete()  
    return asignatura("/show") 

def PapeleraView(request, id_asignatura):  
    asignatura = Asignatura.objects.get(id=id_asignatura)  
    carrera = Carrera.objects.get(id=asignatura.carrera_id)
    planificaciones = Planificacion.objects.filter(asignatura=asignatura).filter(eliminada=True).order_by('id')
   
    return render(request,'asignaturas/papelera.html', {'asignatura':asignatura, 'carrera':carrera, 'planificaciones':planificaciones})   