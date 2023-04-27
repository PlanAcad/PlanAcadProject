from django import forms  
from planificaciones.modelos.modelCorrecciones import Correccion

class CorreccionForm(forms.ModelForm):  
    correccion = forms.CharField(widget=forms.Textarea())
    class Meta:  
        model = Correccion  
        exclude = ['planificacion','creador','usuarioQueResolvio']