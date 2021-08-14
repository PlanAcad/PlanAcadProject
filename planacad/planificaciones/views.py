from django.http import  HttpResponseRedirect
# Para usar los objetos de Request y datetime y redirect
from django.http import  HttpRequest
import datetime
from django.shortcuts import redirect
####

from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
## import model
from .forms import AsignaturaForm 
from .models import Asignatura
##
def IndexView(request):    
    return render(request, 'index.html')
    
##Define request    
def emp(request):  
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