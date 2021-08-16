# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect  
####
## import model and form
from planificaciones.formularios.formAsignatura import AsignaturaForm 
from planificaciones.modelos.modelAsignatura import Asignatura
##
def IndexView(request):    
    return render(request, 'index.html')
    
##Define request for Asignatura   
def asignatura(request):  
    if request.method == "POST":  
        form = AsignaturaForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = AsignaturaForm()  
    return render(request,'index.html',{'form':form}) 

def show(request):  
    asignaturas = Asignatura.objects.all()  
    return render(request,"show.html",{'asignaturas':asignaturas})  
def edit(request, id):  
    asignatura = Asignatura.objects.get(id=id)  
    return render(request,'edit.html', {'asignatura':asignatura})  
def update(request, id):  
    asignatura = Asignatura.objects.get(id=id)  
    form = AsignaturaForm(request.POST, instance = asignatura)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'asignatura': asignatura})  
def destroy(request, id):  
    asignatura = Asignatura.objects.get(id=id)  
    asignatura.delete()  
    return asignatura("/show")  