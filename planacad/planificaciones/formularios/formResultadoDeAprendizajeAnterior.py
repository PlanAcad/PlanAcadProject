from django import forms  
from planificaciones.modelos.modelResultadoDeAprendizajeAnterior import ResultadoDeAprendizajeAnterior, ResultadoDeAprendizajeAnteriorPrimerNivel
from planificaciones.modelos.modelResultadoAprendizaje import ResultadoDeAprendizaje
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelPlanificacion import Planificacion



class ResultadoDeAprendizajeAnteriorForm(forms.ModelForm):

    class Meta:  
        model = ResultadoDeAprendizajeAnterior
        exclude = ['planificacion']
        fields = "__all__"
        
        
        
  
class ResultadoDeAprendizajeAnteriorPrimerNivelForm(forms.ModelForm):

    class Meta:  
        model = ResultadoDeAprendizajeAnteriorPrimerNivel
        exclude = ['planificacion']
        fields = "__all__"
        
        
        