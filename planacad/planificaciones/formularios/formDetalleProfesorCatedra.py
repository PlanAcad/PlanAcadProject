from django import forms  
from django.utils.translation import gettext_lazy as _
from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra

class DetalleProfesorCatedraForm(forms.ModelForm): 
    actividades = forms.CharField(widget=forms.Textarea())
    nombre_profesor = forms.CharField(required=False) 
    apellido_profesor = forms.CharField(required=False) 
    class Meta:  
        model = DetalleProfesorCatedra         
        fields = ['nombre_profesor', 'apellido_profesor', 'profesor', 'categoria', 'situacion', 'dedicacion', 'tareas']
        exclude = ['planificacion']
        widgets = {
            'tareas': forms.CheckboxSelectMultiple()
        }
        labels = {
            'profesor': _('Profesor'),
            'categoria': _('Categoría'),
            'situacion': _('Situación de Revista y/o Condición'),
            'dedicacion': _('Dedicación'),
            'tareas': _('Tareas/Funciones a realizar'),
        }