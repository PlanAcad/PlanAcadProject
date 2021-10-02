from django import forms  
from planificaciones.modelos.modelPlanificacion import Planificacion

class CondicionAprobacionDirectaForm(forms.ModelForm):  
    condicion_aprobacion_directa = forms.CharField(widget=forms.Textarea())
    class Meta:  
        model = Planificacion
        fields = ['condicion_aprobacion_directa']

class CondicionAprobacionCursadaForm(forms.ModelForm):  
    condicion_aprobacion_cursada = forms.CharField(widget=forms.Textarea())
    class Meta:  
        model = Planificacion
        fields = ['condicion_aprobacion_cursada']