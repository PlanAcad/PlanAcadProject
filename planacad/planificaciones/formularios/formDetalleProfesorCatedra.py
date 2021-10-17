from django import forms  
from django.utils.translation import gettext_lazy as _
from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra

class DetalleProfesorCatedraForm(forms.ModelForm): 
    class Meta:  
        model = DetalleProfesorCatedra         
        fields = ['profesor', 'categoria', 'situacion', 'dedicacion', 'tareas']
        exclude = ['actividades', 'planificacion']
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