# Para usar los objetos y/o funciones de 'redirect'

from django.shortcuts import render, redirect  
## import model and form
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.formularios.formPlanificacion import PlanificacionForm

##Define request for Asignatura   
def profesor(request):  
    if request.method == "POST":  
        form = PlanificacionForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = PlanificacionForm()  
    return render(request,'index.html',{'form':form}) 

def PlanificacionesView(request,idAsignatura):
    #Obtengo la asignatura
    asignatura = Asignatura.objects.get(id=idAsignatura)   
    #Busco las planificaciones de esa asignatura
    planificaciones = Planificacion.objects.filter(asignatura=asignatura)
    return render(request,"profesores/index.html",{'planificaciones':planificaciones})  

def PlanificacionDetailView(request, id): 
    planificacion = Planificacion.objects.get(id=id)
    return render(request,'profesores/detail.html', {'planificacion':planificacion})  
 
def PlanificacionUpdate(request, id):  
    planificacion = Planificacion.objects.get(id=id)  
    form = PlanificacionForm(request.POST, instance = planificacion)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'planificacion': planificacion})  

def PlanificacionDestroy(request, id):  
    planificacion = Planificacion.objects.get(id=id)  
    planificacion.delete()  
    return planificacion("/show")  