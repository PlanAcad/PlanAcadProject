from django import forms  
from planificaciones.modelos.modelPlanificacion import Planificacion

class DistribucionTareasForm(forms.ModelForm):  
    class Meta:  
        model = Planificacion
        fields = ['numero_comisiones', 'numero_estudiantes_comision']
