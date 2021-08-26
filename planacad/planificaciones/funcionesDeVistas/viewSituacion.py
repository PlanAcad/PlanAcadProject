# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formSituacion import SituacionForm
from planificaciones.modelos.modelSituacion import Situacion
##Define request for Asignatura   
def NewSituacion(request):  
    if request.method == "POST":  
        form = SituacionForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
            except:  
                pass  
    else:  
        form = SituacionForm()  
    return render(request,'index.html',{'form':form}) 

def SituacionesView(request):  
    situaciones = Situacion.objects.all()  
    return render(request,"",{'situaciones':situaciones})  

def SituacionDetailView(request, id):  
    situacion = Situacion.objects.get(id=id)  
    return render(request,'', {'situacion':situacion})  
 
def SituacionUpdate(request, id):  
    situacion = Situacion.objects.get(id=id)  
    form = SituacionForm(request.POST, instance = situacion)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'situacion': situacion})  

def SituacionDestroy(request, id):  
    situacion = Situacion.objects.get(id=id)  
    situacion.delete()  
    return situacion("/show")  