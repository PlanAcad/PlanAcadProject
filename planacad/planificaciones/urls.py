from django.urls import path

from . import views

app_name = 'planificaciones'
urlpatterns = [
    path('', views.IndexView, name='index'),
    path('asignaturas', views.AsignaturasView, name='asignaturas'),
]