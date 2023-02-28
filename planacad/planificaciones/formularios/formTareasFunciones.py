from django import forms  
from planificaciones.modelos.modelTareasFunciones import TareasFunciones
from django.utils.translation import gettext_lazy as _

class TareasFuncionesForm(forms.ModelForm):
    tarea_funcion = forms.CharField(widget=forms.Textarea())  
    class Meta:  
        model = TareasFunciones  
        fields = "__all__"
        exclude = ["categoria", "planificacion"]
        labels = {
            'tarea_funcion': _('Tarea/Funcion')
        }