# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formCarrera import CarreraForm
from planificaciones.modelos.modelCarrera import Carrera
##Define request for Asignatura   
def profesor(request):  
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

def CarrerasView(request):  
    carreras = Carrera.objects.all()  
    return render(request,"",{'carreras':carreras})  

def CarreraDetailView(request, id):  
    carrera = Carrera.objects.get(id=id)  
    return render(request,'', {'carrera':carrera})  
 
def CarreraUpdate(request, id):  
    carrera = Carrera.objects.get(id=id)  
    form = CarreraForm(request.POST, instance = carrera)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'carrera': carrera})  

def CarreraDestroy(request, id):  
    carrera = Carrera.objects.get(id=id)  
    carrera.delete()  
    return carrera("/show")  