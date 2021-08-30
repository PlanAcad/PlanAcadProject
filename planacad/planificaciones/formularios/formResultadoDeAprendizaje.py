from django import forms  
from planificaciones.modelos.modelResultadoDeAprendizaje import ResultadoDeAprendizaje

class ResultadoDeAprendizajeForm(forms.ModelForm):  
    class Meta:  
        model = ResultadoDeAprendizaje  
        fields = "__all__"