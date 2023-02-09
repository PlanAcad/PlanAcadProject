from django import forms  
from planificaciones.modelos.modelResultadoDeAprendizajeAnterior import ResultadoDeAprendizajeAnterior
from planificaciones.modelos.modelResultadoAprendizaje import ResultadoDeAprendizaje
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelPlanificacion import Planificacion



class ResultadoDeAprendizajeAnteriorForm(forms.ModelForm):

    class Meta:  
        model = ResultadoDeAprendizajeAnterior
        exclude = ['planificacion']
        fields = "__all__"
        
        
        
  