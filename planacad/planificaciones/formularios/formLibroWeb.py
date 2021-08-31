from django import forms  
from planificaciones.modelos.modelLibroWeb import LibroWeb

class LibroWebForm(forms.ModelForm):  
    class Meta:  
        model = LibroWeb  
        fields = "__all__"