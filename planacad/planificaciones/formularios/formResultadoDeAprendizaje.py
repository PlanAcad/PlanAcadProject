from django import forms  
from planificaciones.modelos.modelResultadoDeAprendizaje import ResultadoDeAprendizajes

class ResultadoDeAprendizajeForm(forms.ModelForm):  
    resultado = forms.CharField(widget=forms.Textarea())
    class Meta:  
        model = ResultadoDeAprendizajes  
        exclude = ['planificacion']