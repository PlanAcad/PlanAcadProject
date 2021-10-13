from django import forms  
from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra

class DetalleProfesorCatedraForm(forms.ModelForm): 

    actividades = forms.CharField(widget=forms.Textarea()) 
    nombre_profesor = forms.CharField(required=False) 
    apellido_profesor = forms.CharField(required=False) 
    class Meta:  
        model = DetalleProfesorCatedra  
        exclude = ['planificacion']
        widgets = {
            'tareas': forms.CheckboxSelectMultiple()
        }