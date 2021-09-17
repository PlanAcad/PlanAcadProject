from django.urls import path
from django.shortcuts import render
from planificaciones.funcionesDeVistas import viewProfesor, viewAsignatura, viewLogin,viewPlanificacion, viewSistemaDeEvaluacion 
from . import views

app_name = 'planificaciones'
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('login', viewLogin.LoginView, name='login'),

    #Asignaturas
    path('asignaturas', viewAsignatura.AsignaturasView, name='asignaturas'),
    path('asignaturas/<int:id>', viewAsignatura.AsignaturaDetailView, name='asignaturaDetail'),
    path('asignaturas/<int:asignatura_id>/nueva-planificacion', viewPlanificacion.NewPlanificacion, name='nueva'),

    #Profesor
    path('profesores/<int:id>', viewProfesor.ProfesorDetailView, name='profesorDetail'),

    #Planificacion    
    path('planificacion/<int:id>', viewPlanificacion.PlanificacionDetailView, name='planificacionDetail'),

    #Componentes
    path('componentes', views.ComponentesView, name='componentes'),

    # Seccion 7.1 - Sistema de evaluacion
    path('planificacion/<int:planificacion_id>/sistema-de-evaluacion', viewSistemaDeEvaluacion.SistemaDeEvaluacion, name='sistemaDeEvaluacion'),
    path('planificacion/<int:planificacion_id>/crear-actividad', viewSistemaDeEvaluacion.NewActividad, name='newActividad'),
    path('planificacion/<int:planificacion_id>/actualizar-actividad/<str:actividad_id>', viewSistemaDeEvaluacion.UpdateActividad, name='updateActividad'),
    path('planificacion/<int:planificacion_id>/eliminar-actividad/<str:actividad_id>', viewSistemaDeEvaluacion.DeleteActividad, name='deleteActividad'),




]