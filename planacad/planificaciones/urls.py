from django.urls import path
from planificaciones.funcionesDeVistas import viewProfesor, viewAsignatura, viewLogin,viewPlanificacion, viewSeccion1,viewDetalleProfesorCatedra,viewResultadoDeAprendizaje
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
    
    #Seccion2    
    path('detalles-profesor-catedra/<int:id>', viewDetalleProfesorCatedra.DetallesProfesorCatedraView, name='detallesprofesorcatedra'),

    #Seccion4    
    path('resultados-de-aprendizaje/<int:planificacion_id>', viewResultadoDeAprendizaje.ResultadoDeAprendizajeViewbyPlanificacion, name='resultadosDeAprendizajes'),

]