from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group,User
from planificaciones.modelos.modelCarrera import Carrera
from planificaciones.formularios.registration.formRegistration import CreateUserForm
from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def usersView(request):
    carrera = Carrera.objects.get(id =  request.user.carrera.first().id)
    usuarios = User.objects.all()
    jefeDeCarrera = User.objects.filter(Q(groups = Group.objects.get(name='jefe de carrera')) & Q(carrera = carrera))
    profesores = User.objects.filter(Q(groups = Group.objects.get(name='profesor')) & Q(carrera = carrera))
    consejeros = User.objects.filter(Q(groups = Group.objects.get(name='consejo')) & Q(carrera = carrera))
    alumnos = User.objects.filter(Q(groups = Group.objects.get(name='alumno')) & Q(carrera = carrera))
    
    context = {
    'jefeDeCarrera': jefeDeCarrera,
    'profesores': profesores,
    'consejeros': consejeros,
    'alumnos': alumnos,
    'usuarios': usuarios,
    
     
}
    return render(request,'registration/users.html', context)
