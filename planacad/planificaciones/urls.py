from django.urls import path
from django.shortcuts import render
from . import views
from planificaciones.funcionesDeVistas import viewProfesor, viewAsignatura,viewPlanificacion,viewDetalleProfesorCatedra, viewResultadoDeAprendizaje
from planificaciones.funcionesDeVistas import viewDatosDescriptivos, viewFundamentacion, viewSistemaDeEvaluacion, viewCondicion, viewCompetencia, viewSubCompetencia
from planificaciones.funcionesDeVistas import viewClase
from planificaciones.funcionesDeVistas import viewJustificacionOrdenanza, viewWebgrafia, viewBibliografia, viewResultadoDeApendizajeAnterior, viewDistribucionDeTareas, viewContenido
from planificaciones.funcionesDeVistas import viewPropuestaDesarrollo, viewFechaCalendarioAcademico
from planificaciones.funcionesDeVistas import viewExportar, viewUnidad, viewTareasFunciones, viewUsuarioPlanificacion
from planificaciones.validaciones import validacionSecciones
from planificaciones.CopiarPlanificaciones import copiarPlanificacion
from planificaciones.funcionesDeVistas import viewCorreccion, viewComentarios, viewUsers
from planificaciones.funcionesDeVistas.registration import  viewRegister, viewEditProfile
from django.contrib.auth.views import LoginView,LogoutView
import planificaciones




app_name = 'planificaciones'
urlpatterns = [
    path('', views.IndexView, name='index'),
    #Accounts
    path('login/', LoginView.as_view(), name='login_url'),
    path('register/', viewRegister.registerView, name='register_url'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('users/',viewUsers.usersView,name = "usuarios" ),
    path('users/bulk-create',viewRegister.bulkRegister,name = "Cargarusuarios" ),
    path('users/<int:id>/edit',viewEditProfile.editUserView,name = "edit_profile" ),
    
    #Componentes
    path('componentes', views.ComponentesView, name='componentes'),

    #Asignaturas
    path('asignaturas/', viewAsignatura.AsignaturasView, name='asignaturas'),
    path('asignaturas/bulk-create',viewAsignatura.bulkAsignaturaNew,name = "CargarAsignaturas" ),
    path('asignaturas/<int:id>', viewAsignatura.AsignaturaDetailView, name='asignaturaDetail'),
    path('asignaturas/<int:id>/actualizar', viewAsignatura.AsignaturaUpdate, name='updateAsignatura'),
    path('asignaturas/crear', viewAsignatura.AsignaturaNew, name='newAsignatura'),
    #Asignaturas Detail
    path('asignaturas/<int:id>/<str:error>/', viewAsignatura.AsignaturaDetailView, name='asignaturaDetail'),
    path('asignaturas/<int:asignatura_id>/nueva-planificacion', viewPlanificacion.PlanificacionNew, name='nueva'),
    path('planificacion/<int:id>/eliminar-planif-temporal', viewPlanificacion.PlanificacionLogicDestroy, name='deleteLogicPlanificacion'),
    path('planificacion/<int:id>/recuperar-planificacion',viewPlanificacion.PlanificacionRestore, name='restorePlanificacion'),
    path('planificacion/<int:id>/eliminar-planificacion', viewPlanificacion.PlanificacionDestroy, name='deletePlanificacion'),
    path('planificacion/<int:id_planificacion>/<int:id_asignatura>/subcribirse-planificacion', viewUsuarioPlanificacion.PlanificacionUsuarioNew, name='subcribirsePlanificacion'),
    path('planificacion/<int:id_planificacion>/<int:id_asignatura>/dessubcribirse-planificacion', viewUsuarioPlanificacion.PlanificacionUsuarioDelete, name='dessubcribirsePlanificacion'),


    #Profesor
    path('profesores/', viewProfesor.ProfesorDetailView, name='profesorDetail'),

    #Planificacion    
    path('planificacion/<int:id>', viewPlanificacion.PlanificacionDetailView, name='planificacionDetail'),

    #Calendario Academico    
    path('calendario-academico/<int:ano>', viewFechaCalendarioAcademico.CalendarioAcademicoIndex, name='calendarioacademico'),
    path('calendario-academico/edit/<int:ano>', viewFechaCalendarioAcademico.UpdateFechaCalendarioAcademico, name='updatecalendarioacademico'),
    path('calendario-academico/cerrar/<int:ano>', viewFechaCalendarioAcademico.CerrarCalendarioAcademico, name='cerrarcalendarioacademico'),
    

    ### Secciones ###
    #Seccion 1
    path('planificacion/<int:id_planificacion>/datos-descriptivos/', viewDatosDescriptivos.DatosDescriptivosUpdate, name='datosDescriptivos'),
    path('planificacion/<int:id_planificacion>/datos-descriptivos/Import', viewDatosDescriptivos.ImportDatosDescriptivos, name='importDatosDescriptivos'),
    
    #Seccion2    
    path('planificacion/<int:id_planificacion>/estructura-de-la-catedra', viewDetalleProfesorCatedra.DetalleProfesorCatedraNew, name='detallesprofesorcatedra'),
    path('planificacion/<int:id_planificacion>/estructura-de-la-catedra/ImportData', viewDetalleProfesorCatedra.ImportDetalleProfesorCatedra, name='importDetallesprofesorcatedra'),

    path('planificacion/<int:id_planificacion>/detalles-profesor-catedra/edit/<int:id_detalleprofesorcatedra>', viewDetalleProfesorCatedra.DetalleProfesorCatedraUpdate, name='detallesprofesorcatedraupdate'),
    path('planificacion/<int:id_planificacion>/detalles-profesor-catedra/delete/<int:id_detalleprofesorcatedra>', viewDetalleProfesorCatedra.DetalleProfesorCatedraDestroy, name='detallesprofesorcatedradestroy'),
    path('ajax/load-resultados-profesores/', viewDetalleProfesorCatedra.ProfesoresPorSituacion, name='ajax_load_profesores'),  # <-- this one here
    
    path('planificacion/<int:id_planificacion>/tareas-funciones', viewTareasFunciones.TareasFuncionesNew, name='tareaYFunciones'),
    

    #Seccion 3
    path('planificacion/<int:id_planificacion>/fundamentacion', viewFundamentacion.FundamentacionUpdate, name='fundamentacion'),

    #Seccion4    
    path('planificacion/<int:id_planificacion>/resultados-de-aprendizaje', viewResultadoDeApendizajeAnterior.ResultadoDeAprendizajeAnteriorNew, name='resultadosDeAprendizajes'),
    path('planificacion/<int:id_planificacion>/resultados-de-aprendizaje-manual', viewResultadoDeApendizajeAnterior.ResultadoDeAprendizajeNewFirstPlanificacion, name='resultadosDeAprendizajesPrimeraPlanificacion'),
    
    path('planificacion/<int:id_planificacion>/resultados-de-aprendizaje/edit/<int:id_resultadodeaprendizaje>', viewResultadoDeApendizajeAnterior.ResultadoDeAprendizajeAnteriorUpdate, name='resultadosDeAprendizajesUpdate'),
    path('planificacion/<int:id_planificacion>/resultados-de-aprendizaje/delete/<int:id_resultadodeaprendizaje>', viewResultadoDeApendizajeAnterior.ResultadoDeAprendizajeAnteriorDestroy, name='resultadosDeAprendizajesDestroy'),
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

    # Seccion 7 - Sistema de evaluacion
    path('planificacion/<int:planificacion_id>/sistema-de-evaluacion', viewSistemaDeEvaluacion.SistemaDeEvaluacion, name='sistemaDeEvaluacion'),
    path('planificacion/<int:planificacion_id>/actualizar-actividad/<str:actividad_id>', viewSistemaDeEvaluacion.UpdateActividad, name='updateActividad'),
    path('planificacion/<int:planificacion_id>/eliminar-actividad/<str:actividad_id>', viewSistemaDeEvaluacion.DeleteActividad, name='deleteActividad'),

    # Seccion 7.1 - Condicion de Aprobacion Directa
    path('planificacion/<int:id_planificacion>/condicion-aprobacion-directa', viewCondicion.AprobacionDirecta, name='aprobacionDirecta'),

    # Seccion 7.2 - Condicion de Aprobacion Cursada
    path('planificacion/<int:id_planificacion>/condicion-aprobacion-cursada', viewCondicion.AprobacionCursada, name='aprobacionCursada'),

    # Seccion 8 - Cronogramas
    path('planificacion/<int:id_planificacion>/cronograma', viewClase.ClasesView, name='cronograma'),
    path('planificacion/<int:id_planificacion>/cronograma/edit/<int:id_clase>', viewClase.ClaseUpdate, name='cronogramaUpdate'),
    path('planificacion/<int:id_planificacion>/cronograma/delete/<int:id_clase>', viewClase.ClaseDestroy, name='cronogramaDestroy'),
    path('planificacion/<int:id_planificacion>/cronograma/create', viewClase.CronogramaCreate, name='cronogramaCreate'),
    
    # Seccion 9 - Bibliografia
    path('planificacion/<int:id_planificacion>/bibliografia', viewBibliografia.IndexBibliografia, name='bibliografia'),
    path('planificacion/bibliografia/addFromImport', viewBibliografia.AddBibliografiaFromFile, name='AddBibliografiaFromFile'),

    path('planificacion/<int:id_planificacion>/bibliografia/edit/<int:id_bibliografia>', viewBibliografia.UpdateBibliografia, name='updateBibliografia'),
    path('planificacion/<int:id_planificacion>/bibliografia/delete/<int:id_bibliografia>', viewBibliografia.Deletebibliografia, name='deleteBibliografia'),
    path('ajax/load-bibliografia/', viewBibliografia.ReadBibliografiaFromFile, name='ajax_load_bibliografia'),  # <-- this one here
    
    # Seccion 10 - Webgrafia
    path('planificacion/<int:id_planificacion>/webgrafia', viewWebgrafia.IndexWebgrafia, name='webgrafia'),
    path('planificacion/<int:id_planificacion>/webgrafia/edit/<int:id_webgrafia>', viewWebgrafia.UpdateWebgrafia, name='updateWebgrafia'),
    path('planificacion/<int:id_planificacion>/webgrafia/delete/<int:id_webgrafia>', viewWebgrafia.DeleteWebgrafia, name='deleteWebgrafia'),

    # Seccion 11 - Contenido
    path('planificacion/<int:id_planificacion>/contenido', viewContenido.IndexContenido, name='contenido'),
    path('planificacion/<int:id_planificacion>/contenido/edit/<int:id_contenido>', viewContenido.UpdateContenido, name='updateContenido'),
    path('planificacion/<int:id_planificacion>/contenido/delete/<int:id_contenido>', viewContenido.DeleteContenido, name='deleteContenido'),
    path('planificacion/<int:id_planificacion>/contenido/unidad', viewUnidad.UnidadNew, name='unidad'),
    

    # Seccion 12 - Distribución de tareas
    path('planificacion/<int:id_planificacion>/distribucion-de-tareas', viewDistribucionDeTareas.DistribucionDeTareas, name='distribucionDeTareas'),
    path('planificacion/<int:id_planificacion>/distribucion-de-tareas/edit/<int:id_detalleprofesorcatedra>', viewDistribucionDeTareas.UpdateDistribucionDeTareas, name='updateDistribucionDeTareas'),
    path('planificacion/<int:id_planificacion>/distribucion-de-tareas/delete/<int:id_detalleprofesorcatedra>', viewDistribucionDeTareas.DeleteDistribucionDeTareas, name='deleteDistribucionDeTareas'),
    path('planificacion/<int:id_planificacion>/distribucion-de-tareas-planif', viewDistribucionDeTareas.UpdateDistribucionDeTareasPlanif, name='distribucionTareasPlanif'),
    
 
    # Seccion 13 - Justificacion (Ordenanza 604)
    path('planificacion/<int:id_planificacion>/justificacion-ordenanza', viewJustificacionOrdenanza.JustificacionOrdenanza, name='justificacionOrdenanza'),

    # EXPORTAR PLANIFICACION
    path('planificacion/<int:id_planificacion>/exportar', viewExportar.Exportar, name='exportar'),
    path('planificacion/<int:id_planificacion>/descargar-pdf', viewExportar.DownloadPDF, name='downloadPdf'),
    path('planificacion/<int:id_planificacion>/imprimir-pdf', viewExportar.PrintPDF, name='printPdf'),


   # VALIDACION
    # path('planificacion/<int:id_planificacion>/validacion', validacionSecciones.ValidacionIndex, name='validacionSeccion1'),

   # CREAR PLANIFICACION A PARTIR DE UNA
    path('planificacion/<int:id_planificacion>/planificacion-copiada', copiarPlanificacion.CopiarIndex, name='copiarPlanif'),

   # Estado planificacion
    path('planificacion/<int:id>/cerrar-planificacion', viewPlanificacion.AprobarPlanificacion, name='aprobarPlanif'),
    path('planificacion/<int:id>/revisar-planificacion', viewPlanificacion.RevisarPlanificacion, name='revisarPlanif'),
    path('planificacion/<int:id>/corregir-planificacion', viewPlanificacion.CorregirPlanificacion, name='corregirPlanif'),

    # PAPELERA
    path('asignaturas/<int:id_asignatura>/papelera', viewAsignatura.PapeleraView, name='papelera'),
    
    #Correcciones
    path('planificacion/<int:id_planificacion>/<int:id_seccion>/agregar-correccion', viewCorreccion.CorreccionNew, name='agregarCorreccion'),
    path('planificacion/<int:id_correccion>/resolver-correccion', viewCorreccion.CorreccionUpdate, name='resolverCorreccion'),
    #Comentarios
    path('planificacion/<int:id_correccion>/<int:id_seccion>/agregar-comentario', viewComentarios.ComentarioNew, name='agrergarComentario'),
    #Email
    path('planificacion/mandar-Aviso', viewAsignatura.MandarAvisoFechaLimiteDePlanificacion, name='mandarAviso'),
    
]