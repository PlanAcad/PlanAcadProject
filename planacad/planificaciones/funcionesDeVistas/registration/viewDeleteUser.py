from django.contrib.auth.models import User
from django.shortcuts import redirect

def delete_user(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    return redirect('planificaciones:usuarios')