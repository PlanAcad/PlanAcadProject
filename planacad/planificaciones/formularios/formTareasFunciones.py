from django import forms  
from planificaciones.modelos.modelTareasFunciones import TareasFunciones

class TareasFuncionesForm(forms.ModelForm):  
    class Meta:  
        model = TareasFunciones  
        fields = "__all__"