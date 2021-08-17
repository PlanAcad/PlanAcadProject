from django import forms  
from planificaciones.modelos.modelPlanificacion import Planificacion

class PlanificacionForm(forms.ModelForm):  
    class Meta:  
        model = Planificacion  
        fields = "__all__"