from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from planificaciones.modelos.modelCarrera import Carrera
from planificaciones.formularios.registration.formRegistration import CreateUserForm
from django.shortcuts import render, redirect

def registerView(request):
    if(request.method == 'POST'):
        form = CreateUserForm(request.POST)
        print("guardo")
        if form.is_valid():
            user =form.save()
            group = Group.objects.get(id=request.POST["groups"])
            user.groups.add(group)
            carreras = Carrera.objects.get(id = request.POST["carrera"])
            user.carrera.add(carreras)
            user.save()

            # carreraUser = CarreraUsuario()
            # carreraUser.carrera_id = request.POST["carrera"]
            # carreraUser.usuario_id = user.id
            # carreraUser.save()

            return redirect('planificaciones:usuarios')
        else:
            context = {
            'form': form 
        }
            return render(request,'registration/register.html', context)
    else:
        form = CreateUserForm()
        context = {
            'form': form 
        }
        return render(request,'registration/register.html', context)