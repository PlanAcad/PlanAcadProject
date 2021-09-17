from django import forms  
from planificaciones.modelos.modelCategoria import Categoria

class CategoriaForm(forms.ModelForm):  
    class Meta:  
        model = Categoria  
        fields = "__all__"