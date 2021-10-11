from django import forms  
from planificaciones.modelos.modelBibliografia import Bibliografia

class BibliografiaForm(forms.ModelForm):  
    class Meta:  
        model = Bibliografia  
        exclude = ['planificacion']
        fields = "__all__"