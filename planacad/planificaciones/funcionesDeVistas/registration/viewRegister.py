from django.contrib.auth.forms import UserCreationForm
import pandas as pd
from django.contrib.auth.models import Group
from django.contrib import messages
from planificaciones.modelos.modelCarrera import Carrera
from django.contrib.auth.models import User
from planificaciones.formularios.registration.formRegistration import CreateUserForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
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
            messages.success(request, 'Se ha guardado con éxito')
            return redirect('planificaciones:usuarios')
        else:
            messages.error(request, 'La operación falló')
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

@login_required
def bulkRegister(request):
    if request.method == 'POST':
        try:
            # Obtener el rol del usuario desde el formulario
            role = request.POST.get('role')
            # Leer el archivo Excel y convertirlo en un DataFrame
            df = pd.read_excel(request.FILES['excel_file'],engine='openpyxl')
            df['legajo'] = pd.to_numeric(df['legajo'], errors='coerce').fillna(0).astype(int)
            df['dni'] = pd.to_numeric(df['dni'], errors='coerce').fillna(0).astype(int)
            # Iterar sobre cada fila del DataFrame y crear usuarios de Django
            for _, row in df.iterrows():
                if row['legajo']:
                    user = User.objects.create_user(
                        username= row['legajo'],
                        email=row['email'],
                        password=row['dni'],
                        first_name=row['first_name'],
                        last_name=row['last_name']
                    )
                    group = Group.objects.get(name=role)
                    group.user_set.add(user)
                    carreras = Carrera.objects.get(nombre_carrera = row['carrera'])
                    user.carrera.add(carreras)
                    user.save()
            messages.success(request, 'Se ha guardado con éxito')
        except:  
            messages.error(request, 'La operación falló')

        return redirect('planificaciones:usuarios')