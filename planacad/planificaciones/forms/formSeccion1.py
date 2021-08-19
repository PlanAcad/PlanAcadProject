from django import forms  
from planificaciones.modelos.modelSeccion1 import Seccion1

class Seccion1Form(forms.ModelForm):  
    class Meta:  
        model = Seccion1  
        fields = "__all__"