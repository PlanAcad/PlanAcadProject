from django import forms  
from planificaciones.modelos.modelCondicion import CondicionAprobacionDirecta, CondicionAprobacionCursada

class CondicionAprobacionDirectaForm(forms.ModelForm):  
    descripcion = forms.CharField(widget=forms.Textarea())
    class Meta:  
        model = CondicionAprobacionDirecta
        fields = "__all__"

class CondicionAprobacionCursadaForm(forms.ModelForm):  
    descripcion = forms.CharField(widget=forms.Textarea())
    class Meta:  
        model = CondicionAprobacionCursada
        fields = "__all__"