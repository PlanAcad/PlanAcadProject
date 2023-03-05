from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group,User
from planificaciones.modelos.modelCarrera import Carrera
from planificaciones.formularios.registration.formRegistration import CreateUserForm
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def usersView(request):
    jefeDeCarreraISI,profesoresISI,consejerosISI,alumnosISI = None, None, None, None
    jefeDeCarreraIQ,profesoresIQ,consejerosIQ,alumnosIQ = None, None, None, None
    jefeDeCarreraIEM,profesoresIEM,consejerosIEM,alumnosIEM = None, None, None, None
    jefeDeCarreraLAR,profesoresLAR,consejerosLAR,alumnosLAR = None, None, None, None
    jefeDeCarreraBasicas,profesoresBasicas,consejerosBasicas,alumnosBasicas = None, None, None, None
    
    carrera = Carrera.objects.filter(nombre_carrera="ISI").first()
    if(carrera):
        jefeDeCarreraISI = User.objects.filter(Q(groups = Group.objects.get(name='jefe de carrera')) & Q(carrera = carrera))
        profesoresISI = User.objects.filter(Q(groups = Group.objects.get(name='profesor')) & Q(carrera = carrera))
        consejerosISI = User.objects.filter(Q(groups = Group.objects.get(name='consejo')) & Q(carrera = carrera))
        alumnosISI = User.objects.filter(Q(groups = Group.objects.get(name='alumno')) & Q(carrera = carrera))

    carrera = Carrera.objects.filter(nombre_carrera="IQ").first()
    if(carrera):
        jefeDeCarreraIQ = User.objects.filter(Q(groups = Group.objects.get(name='jefe de carrera')) & Q(carrera = carrera))
        profesoresIQ = User.objects.filter(Q(groups = Group.objects.get(name='profesor')) & Q(carrera = carrera))
        consejerosIQ = User.objects.filter(Q(groups = Group.objects.get(name='consejo')) & Q(carrera = carrera))
        alumnosIQ = User.objects.filter(Q(groups = Group.objects.get(name='alumno')) & Q(carrera = carrera))

    carrera = Carrera.objects.filter(nombre_carrera="IEM").first()
    if(carrera):
        jefeDeCarreraIEM = User.objects.filter(Q(groups = Group.objects.get(name='jefe de carrera')) & Q(carrera = carrera))
        profesoresIEM = User.objects.filter(Q(groups = Group.objects.get(name='profesor')) & Q(carrera = carrera))
        consejerosIEM = User.objects.filter(Q(groups = Group.objects.get(name='consejo')) & Q(carrera = carrera))
        alumnosIEM = User.objects.filter(Q(groups = Group.objects.get(name='alumno')) & Q(carrera = carrera))

    carrera = Carrera.objects.filter(nombre_carrera="LAR").first()
    if(carrera):
        jefeDeCarreraLAR = User.objects.filter(Q(groups = Group.objects.get(name='jefe de carrera')) & Q(carrera = carrera))
        profesoresLAR = User.objects.filter(Q(groups = Group.objects.get(name='profesor')) & Q(carrera = carrera))
        consejerosLAR = User.objects.filter(Q(groups = Group.objects.get(name='consejo')) & Q(carrera = carrera))
        alumnosLAR = User.objects.filter(Q(groups = Group.objects.get(name='alumno')) & Q(carrera = carrera))
 
    carrera = Carrera.objects.filter(nombre_carrera="Basicas").first()
    if(carrera):
        jefeDeCarreraBasicas = User.objects.filter(Q(groups = Group.objects.get(name='jefe de carrera')) & Q(carrera = carrera))
        profesoresBasicas = User.objects.filter(Q(groups = Group.objects.get(name='profesor')) & Q(carrera = carrera))
        consejerosBasicas = User.objects.filter(Q(groups = Group.objects.get(name='consejo')) & Q(carrera = carrera))
        alumnosBasicas = User.objects.filter(Q(groups = Group.objects.get(name='alumno')) & Q(carrera = carrera))
 
    usuarios = User.objects.all()
    # Obtener la lista de roles disponibles desde la base de datos
    roles = Group.objects.values_list('name', flat=True)    
    
    context = {
    'jefeDeCarreraISI': jefeDeCarreraISI,
    'profesoresISI': profesoresISI,
    'consejerosISI': consejerosISI,
    'alumnosISI': alumnosISI,
    'jefeDeCarreraIQ': jefeDeCarreraIQ,
    'profesoresIQ': profesoresIQ,
    'consejerosIQ': consejerosIQ,
    'alumnosIQ': alumnosIQ,
    'jefeDeCarreraIEM': jefeDeCarreraIEM,
    'profesoresIEM': profesoresIEM,
    'consejerosIEM': consejerosIEM,
    'alumnosIEM': alumnosIEM,
    'jefeDeCarreraLAR': jefeDeCarreraLAR,
    'profesoresLAR': profesoresLAR,
    'consejerosLAR': consejerosLAR,
    'alumnosLAR': alumnosLAR,
    'jefeDeCarreraBasicas': jefeDeCarreraBasicas,
    'profesoresBasicas': profesoresBasicas,
    'consejerosBasicas': consejerosBasicas,
    'alumnosBasicas': alumnosBasicas,
    
    'usuarios': usuarios,
    'roles': roles
    
     
}
    return render(request,'registration/users.html', context)
