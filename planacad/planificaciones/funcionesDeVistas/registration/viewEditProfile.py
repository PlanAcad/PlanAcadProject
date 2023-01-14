from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User
from planificaciones.modelos.modelCarrera import Carrera
from planificaciones.formularios.registration.formEditProfile import EditUserForm
from django.shortcuts import render, redirect

def editUserView(request,id):
    user = User.objects.get(id = id)
    if(request.method == 'POST'):
        form = EditUserForm(request.POST, instance = user)
        print("guardo")
        if form.is_valid():
            user =form.save(commit=False)
            group = Group.objects.filter(id=request.POST["groups"])
            user.groups.clear()
            user.groups.set(group)
            carreras = Carrera.objects.filter(id = request.POST["carrera"])
            user.carrera.clear()
            user.carrera.set(carreras)
            user.save()
            return redirect('planificaciones:usuarios')
        else:
            context = {
            'form': form 
        }
            return render(request,'registration/edit_profile.html', context)
    else:
        form = EditUserForm(instance = user)
        context = {
            'form': form 
        }
        return render(request,'registration/edit_profile.html', context)