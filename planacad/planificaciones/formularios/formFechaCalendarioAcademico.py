from django import forms  
from planificaciones.modelos.modelFechaCalendarioAcademico import FechaCalendarioAcademico

class FechaCalendarioAcademicoForm(forms.ModelForm):
      
    class Meta:  
        model = FechaCalendarioAcademico  
        fields = "__all__"