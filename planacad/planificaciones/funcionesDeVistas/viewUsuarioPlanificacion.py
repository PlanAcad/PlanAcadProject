from django.contrib.auth.models import User
from django.contrib import messages
from planificaciones.modelos.modelPlanificacion import Planificacion
from planificaciones.modelos.modelUsuarioPlanificacion import PlanificacionUsuario
from django.shortcuts import render, redirect 


def PlanificacionUsuarioNew(request, id_planificacion,id_asignatura):
    if request.method == 'POST':
        try:
            planificacion = Planificacion.objects.get(pk=id_planificacion)
            usuario = request.user
            planificacion_usuario = PlanificacionUsuario(planificacion=planificacion, usuario=usuario)
            planificacion_usuario.save()
            messages.success(request, 'Se ha realizado con éxito')
        except:  
            messages.error(request, 'La operación falló')
        
        return redirect('planificaciones:asignaturaDetail',id = id_asignatura)


def PlanificacionUsuarioDelete(request, id_planificacion,id_asignatura):
    if request.method == 'POST':
        try:
            planificacionUsuario = PlanificacionUsuario.objects.get(planificacion_id= id_planificacion, usuario_id = request.user.id)
            planificacionUsuario.delete()
            messages.success(request, 'Se ha realizado con éxito')
        except:  
            messages.error(request, 'La operación falló')
        
        return redirect('planificaciones:asignaturaDetail',id = id_asignatura)


