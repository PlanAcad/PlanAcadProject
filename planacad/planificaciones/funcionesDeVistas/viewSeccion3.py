# Para usar los objetos y/o funciones de 'redirect'  
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.modelos.modelSeccion3 import Seccion3
from planificaciones.formularios.formSeccion3 import  Seccion3Form
##Define request for Asignatura   
def Seccion3New():      
        form = Seccion3()
        # Guardo el objeto definitivamente
        form.save()
        # redirect to a new URL:
        return  form

##Este no se deberia usar pero bueno
def Seccion3View(request):  
    secciones3 = Seccion3.objects.all()
    return render(request,"profesores/index.html",{'secciones3':secciones3})  

def Seccion3DetailView(request, id):  
    seccione3 = Seccion3.objects.get(id=id)
    return render(request,'profesores/detail.html', {'seccione3':seccione3})  
 
def Seccion3Update(request, id):  
    seccione3 = Seccion3.objects.get(id=id)  
    form = Seccion3Form(request.POST, instance = seccione3)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'seccione3': seccione3})  

def Seccion3Destroy(request, id):  
    seccione3 = Seccion3.objects.get(id=id)  
    seccione3.delete()  
    return seccione3("/show")  