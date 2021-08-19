from django import forms  
from planificaciones.modelos.modelAsignatura import Asignatura

class AsignaturaForm(forms.ModelForm):  
    class Meta:  
        model = Asignatura  
        fields = "__all__"