from django import forms
from django.utils.translation import ugettext_lazy as _
from planificaciones.modelos.modelContenido import Contenido

class ContenidoForm(forms.ModelForm):  
    objetivos = forms.CharField(widget=forms.Textarea())
    contenido = forms.CharField(widget=forms.Textarea())

    class Meta:  
        model = Contenido  
        exclude = ['planificacion']
        fields = "__all__"
        # labels = {
        #     'autor': _('Autor/es'),
        # }
