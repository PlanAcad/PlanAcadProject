# Para usar los objetos y/o funciones de 'redirect'
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelFechaCalendarioAcademico import FechaCalendarioAcademico
from django.contrib.auth.models import User
from planificaciones.formularios.registration.formRegistration import UserCreationForm
from django.contrib.auth.decorators import login_required


##Define request for Asignatura 
@login_required  
def ProfesorNew(request):  
    if request.method == "POST":  
        form = UserCreationForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = UserCreationForm()  
    return render(request,'index.html',{'form':form}) 

@login_required
def ProfesoresView(request):  
    profesores = User.objects.all()
    return render(request,"profesores/index.html",{'profesores':profesores})  

@login_required
def ProfesorDetailView(request):
    # Obtener materias del profesor
    asignaturas = Asignatura.objects.filter(profesor=request.user)
    calendario = FechaCalendarioAcademico.objects.filter(ciclo_lectivo=datetime.now().year).filter(nombre_mes=datetime.now().strftime("%B")).exclude(actividad='DN').order_by('fecha')
    return render(request,'profesores/detail.html', {'asignaturas':asignaturas, 'calendario': calendario})  

@login_required
def ProfesorUpdate(request, id):  
    profesor = User.objects.get(id=id)  
    form = UserCreationForm(request.POST, instance = profesor)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'profesor': profesor})  

@login_required
def ProfesorDestroy(request, id):  
    profesor = User.objects.get(id=id)  
    profesor.delete()  
    return profesor("/show")  