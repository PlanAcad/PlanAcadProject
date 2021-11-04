from django import forms  
from planificaciones.modelos.modelClase import Clase

class ClaseForm(forms.ModelForm):  
    class Meta:  
        model = Clase  
        exclude = ['planificacion']
        fields = "__all__"