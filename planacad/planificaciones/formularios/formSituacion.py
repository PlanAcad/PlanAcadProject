from django import forms  
from planificaciones.modelos.modelSituacion import Situacion

class SituacionForm(forms.ModelForm):  
    class Meta:  
        model = Situacion  
        fields = "__all__"