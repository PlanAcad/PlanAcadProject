from django import forms  
from planificaciones.modelos.modelSubCompetencia import SubCompetencia

class SubCompetenciaForm(forms.ModelForm):  
    class Meta:  
        model = SubCompetencia  
        fields = "__all__"