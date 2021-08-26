# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
## import model and form
from planificaciones.formularios.formDedicacion import DedicacionForm
from planificaciones.modelos.modelDedicacion import Dedicacion
##Define request for Asignatura   
def NewDedicacion(request):  
    if request.method == "POST":  
        form = DedicacionForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
            except:  
                pass  
    else:  
        form = DedicacionForm()  
    return render(request,'index.html',{'form':form}) 

def DedicacionesView(request):  
    dedicaciones = Dedicacion.objects.all()  
    return render(request,"",{'dedicaciones':dedicaciones})  

def DedicacionDetailView(request, id):  
    dedicacion = Dedicacion.objects.get(id=id)  
    return render(request,'', {'dedicacion':dedicacion})  
 
def DedicacionUpdate(request, id):  
    dedicacion = Dedicacion.objects.get(id=id)  
    form = DedicacionForm(request.POST, instance = dedicacion)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'dedicacion': dedicacion})  

def DedicacionDestroy(request, id):  
    dedicacion = Dedicacion.objects.get(id=id)  
    dedicacion.delete()  
    return dedicacion("/show")  