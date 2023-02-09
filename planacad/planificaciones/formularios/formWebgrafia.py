from django import forms
from django.utils.translation import ugettext_lazy as _
from planificaciones.modelos.modelWebgrafia import Webgrafia

class WebgrafiaForm(forms.ModelForm):  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_publicacion'].widget.attrs.update({'placeholder': 'DD/MM/AAAA'})

    class Meta:  
        model = Webgrafia  
        exclude = ['planificacion']
        fields = "__all__"
        labels = {
            'autor': _('Autor/es'),
        }
