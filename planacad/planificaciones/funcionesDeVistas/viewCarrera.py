# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formCarrera import CarreraForm
from planificaciones.modelos.modelCarrera import Carrera
from django.contrib.auth.decorators import login_required


##Define request for Asignatura   
@login_required
def CarreraNew(request):  
    if request.method == "POST":  
        form = CarreraForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = CarreraForm()  
    return render(request,'index.html',{'form':form}) 

@login_required
def CarrerasView(request):  
    carreras = Carrera.objects.all()  
    return render(request,"",{'carreras':carreras})  

@login_required
def CarreraDetailView(request, id):  
    carrera = Carrera.objects.get(id=id)  
    return render(request,'', {'carrera':carrera})  

@login_required
def CarreraUpdate(request, id):  
    carrera = Carrera.objects.get(id=id)  
    form = CarreraForm(request.POST, instance = carrera)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'carrera': carrera})  

@login_required
def CarreraDestroy(request, id):  
    carrera = Carrera.objects.get(id=id)  
    carrera.delete()  
    return carrera("/show")  