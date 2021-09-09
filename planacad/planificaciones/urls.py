from django.urls import path
from planificaciones.funcionesDeVistas import viewProfesor, viewAsignatura, viewLogin,viewPlanificacion,viewDetalleProfesorCatedra,viewResultadoDeAprendizaje
from django.shortcuts import render
from planificaciones.funcionesDeVistas import viewProfesor, viewAsignatura, viewLogin,viewPlanificacion, viewDatosDescriptivos, viewFundamentacion
from . import views

app_name = 'planificaciones'
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('login', viewLogin.LoginView, name='login'),

    #Asignaturas
    path('asignaturas', viewAsignatura.AsignaturasView, name='asignaturas'),
    path('asignaturas/<int:id>', viewAsignatura.AsignaturaDetailView, name='asignaturaDetail'),
    path('asignaturas/<int:asignatura_id>/nueva-planificacion', viewPlanificacion.PlanificacionNew, name='nueva'),

    #Profesor
    path('profesores/<int:id>', viewProfesor.ProfesorDetailView, name='profesorDetail'),

    #Planificacion    
    path('planificacion/<int:id>', viewPlanificacion.PlanificacionDetailView, name='planificacionDetail'),
    

    ### Secciones ###
    #Seccion 1
    path('planificacion/<int:id_planificacion>/datos-descriptivos', viewDatosDescriptivos.DatosDescriptivosUpdate, name='datos-descriptivos'),
    #Seccion2    
    path('planificacion/<int:id_planificacion>/estructura-de-la-catedra', viewDetalleProfesorCatedra.DetalleProfesorCatedraNew, name='detallesprofesorcatedra'),
    path('planificacion/<int:id_planificacion>/detalles-profesor-catedra/edit/<int:id_detalleprofesorcatedra>', viewDetalleProfesorCatedra.DetalleProfesorCatedraUpdate, name='detallesprofesorcatedraupdate'),
    path('planificacion/<int:id_planificacion>/detalles-profesor-catedra/delete/<int:id_detalleprofesorcatedra>', viewDetalleProfesorCatedra.DetalleProfesorCatedraDestroy, name='detallesprofesorcatedradestroy'),
    #Seccion 3
    path('planificacion/<int:id_planificacion>/fundamentacion', viewFundamentacion.FundamentacionUpdate, name='fundamentacion'),
    #Seccion4    
    path('planificacion/<int:id_planificacion>/resultados-de-aprendizaje', viewResultadoDeAprendizaje.ResultadoDeAprendizajeNew, name='resultadosDeAprendizajes'),

    #Componentes
    path('componentes', views.ComponentesView, name='componentes'),
]