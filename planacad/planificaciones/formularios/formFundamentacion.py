from django import forms  
from planificaciones.modelos.modelFundamentacion import Fundamentacion

class FundamentacionForm(forms.ModelForm):  
    fundamentos = forms.CharField(widget=forms.Textarea())
    class Meta:  
        model = Fundamentacion
        fields = "__all__"