from django import forms  
from planificaciones.modelos.modelUnidad import Unidad

class UnidadForm(forms.ModelForm):  
    class Meta:  
        model = Unidad  
        fields = "__all__"