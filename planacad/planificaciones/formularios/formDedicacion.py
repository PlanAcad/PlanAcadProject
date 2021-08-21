from django import forms  
from planificaciones.modelos.modelDedicacion import Dedicacion

class DedicacionForm(forms.ModelForm):  
    class Meta:  
        model = Dedicacion  
        fields = "__all__"