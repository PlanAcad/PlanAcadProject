from django.urls import path
from django.shortcuts import render
from . import views
from planificaciones.funcionesDeVistas import viewProfesor, viewAsignatura, viewLogin,viewPlanificacion,viewDetalleProfesorCatedra, viewResultadoDeAprendizaje, viewDatosDescriptivos, viewFundamentacion, viewSistemaDeEvaluacion, viewCondicion, viewCompetencia, viewSubCompetencia


app_name = 'planificaciones'
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('login', viewLogin.LoginView, name='login'),

    #Asignaturas
    path('asignaturas', viewAsignatura.AsignaturasView, name='asignaturas'),
    path('asignaturas/<int:id>', viewAsignatura.AsignaturaDetailView, name='asignaturaDetail'),
    path('asignaturas/<int:asignatura_id>/nueva-planificacion', viewPlanificacion.PlanificacionNew, name='nueva'),
    path('planificacion/<int:id>/eliminar-planificacion', viewPlanificacion.PlanificacionLogicDestroy, name='eliminar'),

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
    path('planificacion/<int:id_planificacion>/resultados-de-aprendizaje/edit/<int:id_resultadodeaprendizaje>', viewResultadoDeAprendizaje.ResultadoDeAprendizajeUpdate, name='resultadosDeAprendizajesUpdate'),
    path('planificacion/<int:id_planificacion>/resultados-de-aprendizaje/delete/<int:id_resultadodeaprendizaje>', viewResultadoDeAprendizaje.ResultadoDeAprendizajeDestroy, name='resultadosDeAprendizajesDestroy'),

    #Seccion5 - Competencias y capacidades vinculadas con la asignatura    
    path('planificacion/<int:id_planificacion>/competencias', viewCompetencia.CompetenciaNew, name='competencias'),
    path('planificacion/<int:id_planificacion>/competencias/edit/<int:id_competencia>', viewCompetencia.CompetenciaUpdate, name='competenciaUpdate'),
    path('planificacion/<int:id_planificacion>/competencias/delete/<int:id_competencia>', viewCompetencia.CompetenciaDestroy, name='competenciaDestroy'),

    path('planificacion/<int:id_planificacion>/competencias/<int:id_competencia>/subcompetencias', viewSubCompetencia.SubCompetenciaNew, name='subcompetencias'),
    path('planificacion/<int:id_planificacion>/competencias/<int:id_competencia>/subcompetencias/edit/<int:id_subcompetencia>', viewSubCompetencia.SubCompetenciaUpdate, name='subcompetenciasUpdate'),
    path('planificacion/<int:id_planificacion>/competencias/<int:id_competencia>/subcompetencias/delete/<int:id_subcompetencia>', viewSubCompetencia.SubCompetenciaDestroy, name='subcompetenciasDestroy'),


    #Componentes
    path('componentes', views.ComponentesView, name='componentes'),

    # Seccion 7 - Sistema de evaluacion
    path('planificacion/<int:planificacion_id>/sistema-de-evaluacion', viewSistemaDeEvaluacion.SistemaDeEvaluacion, name='sistemaDeEvaluacion'),
    path('planificacion/<int:planificacion_id>/crear-actividad', viewSistemaDeEvaluacion.NewActividad, name='newActividad'),
    path('planificacion/<int:planificacion_id>/actualizar-actividad/<str:actividad_id>', viewSistemaDeEvaluacion.UpdateActividad, name='updateActividad'),
    path('planificacion/<int:planificacion_id>/eliminar-actividad/<str:actividad_id>', viewSistemaDeEvaluacion.DeleteActividad, name='deleteActividad'),

    # Seccion 7.1 - Condicion de Aprobacion Directa
    path('planificacion/<int:id_planificacion>/condicion-aprobacion-directa', viewCondicion.AprobacionDirecta, name='aprobacionDirecta'),

    # Seccion 7.2 - Condicion de Aprobacion Cursada
    path('planificacion/<int:id_planificacion>/condicion-aprobacion-cursada', viewCondicion.AprobacionCursada, name='aprobacionCursada'),


]