from django import forms  
from planificaciones.modelos.modelContenido import Contenido

class ContenidoForm(forms.ModelForm):  
    class Meta:  
        model = Contenido  
        fields = "__all__"