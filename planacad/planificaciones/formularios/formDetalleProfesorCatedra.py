from django import forms  
from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra

class DetalleProfesorCatedraForm(forms.ModelForm): 

    actividades = forms.CharField(widget=forms.Textarea()) 
    class Meta:  
        model = DetalleProfesorCatedra  
        exclude = ['planificacion']
        widgets = {
            'tareas': forms.CheckboxSelectMultiple()
        }