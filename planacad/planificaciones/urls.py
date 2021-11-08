from django.urls import path
from django.shortcuts import render
from . import views
from planificaciones.funcionesDeVistas import viewProfesor, viewAsignatura, viewLogin,viewPlanificacion,viewDetalleProfesorCatedra, viewResultadoDeAprendizaje
from planificaciones.funcionesDeVistas import viewDatosDescriptivos, viewFundamentacion, viewSistemaDeEvaluacion, viewCondicion, viewCompetencia, viewSubCompetencia
from planificaciones.funcionesDeVistas import viewJustificacionOrdenanza, viewWebgrafia, viewBibliografia, viewResultadoDeApendizajeAnterior, viewDistribucionDeTareas, viewContenido
from planificaciones.funcionesDeVistas import viewPropuestaDesarrollo




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
    path('planificacion/<int:id_planificacion>/resultados-de-aprendizaje', viewResultadoDeApendizajeAnterior.ResultadoDeAprendizajeAnteriorNew, name='resultadosDeAprendizajes'),
    path('planificacion/<int:id_planificacion>/resultados-de-aprendizaje/edit/<int:id_resultadodeaprendizaje>', viewResultadoDeAprendizaje.ResultadoDeAprendizajeUpdate, name='resultadosDeAprendizajesUpdate'),
    path('planificacion/<int:id_planificacion>/resultados-de-aprendizaje/delete/<int:id_resultadodeaprendizaje>', viewResultadoDeAprendizaje.ResultadoDeAprendizajeDestroy, name='resultadosDeAprendizajesDestroy'),
    path('ajax/load-resultados/', viewResultadoDeApendizajeAnterior.ResultadosDeAprendizajePorAsignatura, name='ajax_load_resultados'),  # <-- this one here
    
    #Seccion5 - Competencias y capacidades vinculadas con la asignatura    
    path('planificacion/<int:id_planificacion>/competencias', viewCompetencia.CompetenciaNew, name='competencias'),
    path('planificacion/<int:id_planificacion>/competencias/edit/<int:id_competencia>', viewCompetencia.CompetenciaUpdate, name='competenciaUpdate'),
    path('planificacion/<int:id_planificacion>/competencias/delete/<int:id_competencia>', viewCompetencia.CompetenciaDestroy, name='competenciaDestroy'),

    path('planificacion/<int:id_planificacion>/competencias/<int:id_competencia>/subcompetencias', viewSubCompetencia.SubCompetenciaNew, name='subcompetencias'),
    path('planificacion/<int:id_planificacion>/competencias/<int:id_competencia>/subcompetencias/edit/<int:id_subcompetencia>', viewSubCompetencia.SubCompetenciaUpdate, name='subcompetenciasUpdate'),
    path('planificacion/<int:id_planificacion>/competencias/<int:id_competencia>/subcompetencias/delete/<int:id_subcompetencia>', viewSubCompetencia.SubCompetenciaDestroy, name='subcompetenciasDestroy'),

    # Seccion 6 - Propuestas para el desarrollo
    path('planificacion/<int:id_planificacion>/propuesta-desarrollo', viewPropuestaDesarrollo.IndexPropuestaDesarrollo, name='propuestaDesarrollo'),
    path('planificacion/<int:id_planificacion>/propuesta-desarrollo/edit/resultado-aprendizaje/<int:id_resultado_aprendizaje>', viewPropuestaDesarrollo.UpdateResultadoAprendizaje, name='updatePDResultadoAprendizaje'),
    path('planificacion/<int:id_planificacion>/propuesta-desarrollo/delete/resultado-aprendizaje/<int:id_resultado_aprendizaje>', viewPropuestaDesarrollo.DeleteResultadoAprendizaje, name='deletePDResultadoAprendizaje'),

    path('planificacion/<int:id_planificacion>/propuesta-desarrollo/edit/<int:id_propuesta_desarrollo>', viewPropuestaDesarrollo.UpdatePropuestaDesarrollo, name='updatePropuestaDesarrollo'),
    path('planificacion/<int:id_planificacion>/propuesta-desarrollo/delete/<int:id_propuesta_desarrollo>', viewPropuestaDesarrollo.DeletePropuestaDesarrollo, name='deletePropuestaDesarrollo'),




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

    # Seccion 9 - Bibliografia
    path('planificacion/<int:id_planificacion>/bibliografia', viewBibliografia.IndexBibliografia, name='bibliografia'),
    path('planificacion/<int:id_planificacion>/bibliografia/edit/<int:id_bibliografia>', viewBibliografia.UpdateBibliografia, name='updateBibliografia'),
    path('planificacion/<int:id_planificacion>/bibliografia/delete/<int:id_bibliografia>', viewBibliografia.Deletebibliografia, name='deleteBibliografia'),

    # Seccion 10 - Webgrafia
    path('planificacion/<int:id_planificacion>/webgrafia', viewWebgrafia.IndexWebgrafia, name='webgrafia'),
    path('planificacion/<int:id_planificacion>/webgrafia/edit/<int:id_webgrafia>', viewWebgrafia.UpdateWebgrafia, name='updateWebgrafia'),
    path('planificacion/<int:id_planificacion>/webgrafia/delete/<int:id_webgrafia>', viewWebgrafia.DeleteWebgrafia, name='deleteWebgrafia'),

    # Seccion 11 - Contenido
    path('planificacion/<int:id_planificacion>/contenido', viewContenido.IndexContenido, name='contenido'),
    path('planificacion/<int:id_planificacion>/contenido/edit/<int:id_contenido>', viewContenido.UpdateContenido, name='updateContenido'),
    path('planificacion/<int:id_planificacion>/contenido/delete/<int:id_contenido>', viewContenido.DeleteContenido, name='deleteContenido'),

    # Seccion 12 - Distribución de tareas
    path('planificacion/<int:id_planificacion>/distribucion-de-tareas', viewDistribucionDeTareas.DistribucionDeTareas, name='distribucionDeTareas'),
    path('planificacion/<int:id_planificacion>/distribucion-de-tareas/edit/<int:id_detalleprofesorcatedra>', viewDistribucionDeTareas.UpdateDistribucionDeTareas, name='updateDistribucionDeTareas'),
    path('planificacion/<int:id_planificacion>/distribucion-de-tareas/delete/<int:id_detalleprofesorcatedra>', viewDistribucionDeTareas.DeleteDistribucionDeTareas, name='deleteDistribucionDeTareas'),
    

    # Seccion 13 - Justificacion (Ordenanza 604)
    path('planificacion/<int:id_planificacion>/justificacion-ordenanza', viewJustificacionOrdenanza.JustificacionOrdenanza, name='justificacionOrdenanza'),


]