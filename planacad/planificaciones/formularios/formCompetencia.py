from django import forms  
from planificaciones.modelos.modelCompetencia import Competencia

class CompetenciaForm(forms.ModelForm):  
    class Meta:  
        model = Competencia  
        fields = "__all__"