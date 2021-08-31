from django import forms  
from planificaciones.modelos.modelLibro import Libro

class LibroForm(forms.ModelForm):  
    class Meta:  
        model = Libro  
        fields = "__all__"