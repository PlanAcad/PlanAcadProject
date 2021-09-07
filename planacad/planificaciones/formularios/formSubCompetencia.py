from django import forms  
from planificaciones.modelos.modelSubCompetencia import SubCompetencia

class CompetenciaForm(forms.ModelForm):  
    class Meta:  
        model = SubCompetencia  
        fields = "__all__"