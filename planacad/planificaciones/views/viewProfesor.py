# Para usar los objetos y/o funciones de 'redirect'

from django.shortcuts import render, redirect  
## import model and form
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelProfesor import Profesor
from planificaciones.forms.formProfesores import  ProfesorForm
##Define request for Asignatura   
def profesor(request):  
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

def ProfesorDetailView(request, id):  
    profesor = Profesor.objects.get(id=id)
    # Obtener materias del profesor
    asignaturas = Asignatura.objects.filter(profesor=profesor)
    return render(request,'profesores/detail.html', {'profesor':profesor, 'asignaturas':asignaturas})  
 
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