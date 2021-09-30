from django import forms  
from planificaciones.modelos.modelResultadoAprendizaje import ResultadoDeAprendizaje

class ResultadoDeAprendizajeForm(forms.ModelForm):  
    resultado = forms.CharField(widget=forms.Textarea())
    class Meta:  
        model = ResultadoDeAprendizaje  
        exclude = ['planificacion']