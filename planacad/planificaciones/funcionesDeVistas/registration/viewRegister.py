from django.contrib.auth.forms import UserCreationForm
from planificaciones.formularios.registration.formRegistration import CreateUserForm
from django.shortcuts import render, redirect

def registerView(request):
    if(request.method == 'POST'):
        form = CreateUserForm(request.POST)
        print("guardo")
        if form.is_valid():
            form.save()
            return redirect('planificaciones:login_url')
        else:
            context = {
            'form': form 
        }
            return render(request,'registration/register.html', context)
    else:
        print("no guardo")
        form = CreateUserForm()
        context = {
            'form': form 
        }
        return render(request,'registration/register.html', context)