from django import forms  
from django.utils.translation import ugettext_lazy as _
from planificaciones.modelos.modelBibliografia import Bibliografia

class BibliografiaForm(forms.ModelForm):  
    class Meta:  
        model = Bibliografia  
        exclude = ['planificacion']
        fields = "__all__"
        labels = {
            'autor': _('Autor/es'),
            'editor': _('Editor/es'),
        }
