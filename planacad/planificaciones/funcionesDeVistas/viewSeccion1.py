# Para usar los objetos y/o funciones de 'redirect'  
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.modelos.modelSeccion1 import Seccion1
from planificaciones.formularios.formSeccion1 import  Seccion1Form
##Define request for Asignatura   
def Newseccion1(request,asignatura_id, carrera_id):  
    if request.method == "POST":  
        form = Seccion1Form(request.POST)  
        # check whether it's valid:
        if form.is_valid():
            print("form valid")
            # Creo una instancia y no lo guardo aun
            instance = form.save(commit=False)
            # Asigno la asignatura y carrera, no hace falta ir a buscar el objeto
            instance.asignatura_id = asignatura_id
            instance.carrera_id = carrera_id
            # Guardo el objeto definitivamente
            instance.save()
            # redirect to a new URL:
            return  instance.id
        # if a GET (or any other method) we'll create a blank form 
        else:  
            form = Seccion1Form()  
    return render(request,'index.html',{'form':form})

##Este no se deberia usar pero bueno
def Seccion1View(request):  
    secciones1 = Seccion1.objects.all()
    return render(request,"profesores/index.html",{'secciones1':secciones1})  

def Seccion1DetailView(request, id):  
    seccion1 = Seccion1.objects.get(id=id)
    return render(request,'profesores/detail.html', {'seccion1':seccion1})  
 
def Seccion1Update(request, id):  
    seccion1 = Seccion1.objects.get(id=id)  
    form = Seccion1Form(request.POST, instance = seccion1)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'seccion1': seccion1})  

def Seccion1Destroy(request, id):  
    seccion1 = Seccion1.objects.get(id=id)  
    seccion1.delete()  
    return seccion1("/show")  