from django import forms  
from planificaciones.modelos.modelResultadoDeAprendizajeAnterior import ResultadoDeAprendizajeAnterior
from planificaciones.modelos.modelResultadoAprendizaje import ResultadoDeAprendizaje


class ResultadoDeAprendizajeAnteriorForm(forms.ModelForm):  
    class Meta:  
        model = ResultadoDeAprendizajeAnterior
        exclude = ['planificacion']
        fields = "__all__"
  