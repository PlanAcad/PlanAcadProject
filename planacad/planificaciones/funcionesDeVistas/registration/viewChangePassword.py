from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from planificaciones.formularios.registration.formCambiarContraseña import CambiarContraseñaForm

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })

@login_required
def cambiarContraseñaAdmin(request, user_id):
    if request.user.is_superuser: # Verificar si el usuario actual es un superusuario
        usuario = User.objects.get(id=user_id)
        form = CambiarContraseñaForm()
        if request.method == 'POST':
            form = CambiarContraseñaForm(request.POST)
            if form.is_valid():
                nueva_contraseña = form.cleaned_data['nueva_contraseña']
                confirmar_contraseña = form.cleaned_data['confirmar_contraseña']
                if nueva_contraseña == confirmar_contraseña:
                    usuario.set_password(nueva_contraseña)
                    usuario.save()
                    messages.success(request, f"La contraseña del usuario {usuario.username} ha sido cambiada.")
                    return redirect('planificaciones:edit_profile',id = user_id) # Redirigir a la página de inicio
                else:
                    messages.error(request, "Las contraseñas no coinciden. Por favor, inténtalo de nuevo.")
        return render(request, 'registration/change_password.html', {'form': form, 'usuario':usuario})            
    else:
        messages.error(request, "No tienes permiso para cambiar la contraseña de otros usuarios.")
        return redirect('planificaciones:edit_profile',id = user_id) # Redirigir a la página de inicio