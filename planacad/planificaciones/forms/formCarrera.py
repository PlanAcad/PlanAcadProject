from django import forms  
from planificaciones.modelos.modelCarrera import Carrera

class CarreraForm(forms.ModelForm):  
    class Meta:  
        model = Carrera  
        fields = "__all__"