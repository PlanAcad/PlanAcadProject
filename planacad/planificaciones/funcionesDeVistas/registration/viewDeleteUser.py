from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages

def delete_user(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    messages.success(request, 'Se ha eliminado con éxito')
    return redirect('planificaciones:usuarios')