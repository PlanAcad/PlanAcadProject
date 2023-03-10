from django.contrib.auth.models import Group, User
from planificaciones.modelos.modelCarrera import Carrera
from planificaciones.formularios.registration.formEditProfile import EditUserForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def editUserView(request,id):
    user = User.objects.get(id = id)
    if(request.method == 'POST'):
        form = EditUserForm(request.POST, instance = user)
        if form.is_valid():
            user =form.save(commit=False)
            group = Group.objects.filter(id=request.POST["groups"])
            print(group)
            user.groups.clear()
            user.groups.set(group)
            carreras = Carrera.objects.filter(id = request.POST["carrera"])
            print(carreras)
            user.carrera.clear()
            user.carrera.set(carreras)
            user.save()
            return redirect('planificaciones:usuarios')
        else:

            form.fields['rol'].initial = user.groups.all().first()
            form.fields['carrera'].initial = user.carrera.all().first()

            context = {
            'user': user,
            'form': form 
        }
            return render(request,'registration/edit_profile.html', context)
    else:
        form = EditUserForm(instance = user)

        print(user.groups.all().first())
        print(user.groups.all().first().id)
        
        form.fields['carrera'].initial = user.carrera.all().first()
        form.fields['rol'].initial = user.groups.all().first() or None
        print(form.fields)
        
        context = {
            'user': user,
            'form': form 
        }
        return render(request,'registration/edit_profile.html', context)