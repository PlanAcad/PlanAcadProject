# Para usar los objetos y/o funciones de 'redirect'
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelFechaCalendarioAcademico import FechaCalendarioAcademico
from planificaciones.modelos.modelProfesor import Profesor
from planificaciones.formularios.formProfesores import  ProfesorForm
##Define request for Asignatura   
def ProfesorNew(request):  
    if request.method == "POST":  
        form = ProfesorForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ProfesorForm()  
    return render(request,'index.html',{'form':form}) 

def ProfesoresView(request):  
    profesores = Profesor.objects.all()
    return render(request,"profesores/index.html",{'profesores':profesores})  

@login_required
def ProfesorDetailView(request, id):  
    profesor = Profesor.objects.get(id=id)
    # Obtener materias del profesor
    asignaturas = Asignatura.objects.filter(profesor=profesor)
    calendario = FechaCalendarioAcademico.objects.filter(ciclo_lectivo=datetime.now().year).filter(nombre_mes=datetime.now().strftime("%B")).exclude(actividad='DN').order_by('fecha')
    return render(request,'profesores/detail.html', {'profesor':profesor, 'asignaturas':asignaturas, 'calendario': calendario})  
 
def ProfesorUpdate(request, id):  
    profesor = Profesor.objects.get(id=id)  
    form = ProfesorForm(request.POST, instance = profesor)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'profesor': profesor})  

def ProfesorDestroy(request, id):  
    profesor = Profesor.objects.get(id=id)  
    profesor.delete()  
    return profesor("/show")  