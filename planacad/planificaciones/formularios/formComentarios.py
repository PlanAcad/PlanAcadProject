from django import forms  
from planificaciones.modelos.modelComentarios import Comentario

class ComentarioForm(forms.ModelForm):  
    comentario = forms.CharField(widget=forms.Textarea())
    class Meta:  
        model = Comentario  
        exclude = ['planificacion']