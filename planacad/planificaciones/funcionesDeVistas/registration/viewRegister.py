from django.contrib.auth.forms import UserCreationForm
import pandas as pd
from django.contrib.auth.models import Group
from planificaciones.modelos.modelCarrera import Carrera
from django.contrib.auth.models import User
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

def bulkRegister(request):
    if request.method == 'POST':
        # Obtener el rol del usuario desde el formulario
        role = request.POST.get('role')
        print(role)
        # Leer el archivo Excel y convertirlo en un DataFrame
        df = pd.read_excel(request.FILES['excel_file'],engine='openpyxl')
        # Iterar sobre cada fila del DataFrame y crear usuarios de Django
        for _, row in df.iterrows():
            user = User.objects.create_user(
                username= row['first_name']+row['last_name'],
                email=row['email'],
                password=row['dni'],
                first_name=row['first_name'],
                last_name=row['last_name'],
            )
            group = Group.objects.get(name=role)
            group.user_set.add(user)
            carreras = Carrera.objects.get(nombre_carrera = row['carrera'])
            user.carrera.add(carreras)
            user.save()
        return redirect('planificaciones:usuarios')