from django import forms  
from planificaciones.modelos.modelCompetencia import Competencia

class CompetenciaForm(forms.ModelForm):  
    class Meta:  
        model = Competencia  
        exclude = ['planificacion']
        widgets = {
            'descripcion': forms.Textarea()
        }