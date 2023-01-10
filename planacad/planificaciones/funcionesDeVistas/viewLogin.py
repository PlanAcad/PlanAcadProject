
# Para usar los objetos y/o funciones de 'redirect'
from django.shortcuts import render, redirect 
## import model and form
from planificaciones.modelos.modelProfesor import Profesor



def LoginView(request):  
    profesores = Profesor.objects.all()  
    return render(request,"login.html",{'profesores':profesores})  