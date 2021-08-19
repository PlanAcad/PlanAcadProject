from django import forms  
from planificaciones.modelos.modelProfesor import Profesor

class ProfesorForm(forms.ModelForm):  
    class Meta:  
        model = Profesor  
        fields = "__all__"