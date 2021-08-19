
# Para usar los objetos y/o funciones de 'redirect'
from planificaciones.forms.formPlanificacion import PlanificacionForm
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.forms.formAsignatura import AsignaturaForm 
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelCarrera import Carrera
from planificaciones.modelos.modelPlanificacion import Planificacion

##Define request for Asignatura   
def asignatura(request):  
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
    planificaciones = Planificacion.objects.filter(asignatura=asignatura)
    # Mandarle el form para crear planificaciones
    form = PlanificacionForm()  
    return render(request,'asignaturas/detail.html', {'asignatura':asignatura, 'carrera':carrera, 'planificaciones':planificaciones, 'form':form})  
 
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