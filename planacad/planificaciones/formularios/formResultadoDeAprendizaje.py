from django import forms  
from planificaciones.modelos.modelResultadoDeAprendizaje import ResultadoDeAprendizaje

class ResultadoDeAprendizajeForm(forms.ModelForm):  
    resultado = forms.CharField(widget=forms.Textarea())
    class Meta:  
        model = ResultadoDeAprendizaje  
        exclude = ['planificacion']