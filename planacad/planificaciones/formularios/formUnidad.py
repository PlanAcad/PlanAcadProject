from django import forms  
from planificaciones.modelos.modelUnidad import Unidad

class ProfesorForm(forms.ModelForm):  
    class Meta:  
        model = Unidad  
        fields = "__all__"