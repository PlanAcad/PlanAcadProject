from django import forms  
from planificaciones.modelos.modelSeccion3 import Seccion3

class Seccion3Form(forms.ModelForm):  
    fundamentos = forms.CharField(widget=forms.Textarea())
    class Meta:  
        model = Seccion3
        fields = "__all__"