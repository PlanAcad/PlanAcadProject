from django import forms  
from planificaciones.modelos.modelPlanificacion import Planificacion

class JustificacionOrdenanzaForm(forms.ModelForm):  
    justificacion_ordenanza = forms.CharField(widget=forms.Textarea())
    class Meta:  
        model = Planificacion
        fields = ['justificacion_ordenanza']

