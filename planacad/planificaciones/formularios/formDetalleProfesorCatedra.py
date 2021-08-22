from django import forms  
from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra

class DetalleProfesorCatedraForm(forms.ModelForm):  
    class Meta:  
        model = DetalleProfesorCatedra  
        fields = "__all__"