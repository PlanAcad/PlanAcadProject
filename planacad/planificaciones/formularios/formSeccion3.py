from django import forms  
from planificaciones.modelos.modelSeccion3 import Seccion3

class Seccion3Form(forms.ModelForm):  
    class Meta:  
        model = Seccion3
        fields = "__all__"