from django import forms  
from planificaciones.modelos.modelResultadoDeAprendizajeAnterior import ResultadoDeAprendizajeAnterior

class ResultadoDeAprendizajeAnteriorForm(forms.ModelForm):  
    class Meta:  
        model = ResultadoDeAprendizajeAnterior
        fields = "__all__"  