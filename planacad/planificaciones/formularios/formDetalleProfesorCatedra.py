from django import forms 
from django.contrib.auth.models import User, Group 
from django.utils.translation import gettext_lazy as _
from planificaciones.modelos.modelDetalleProfesorCatedra import DetalleProfesorCatedra
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelTareasFunciones import TareasFunciones



class DetalleProfesorCatedraForm(forms.ModelForm):
    profesor = forms.ModelChoiceField(
        queryset= User.objects.filter(groups= Group.objects.get(name='profesor')))
    
    
    nombre_profesor = forms.CharField(required=False) 
    apellido_profesor = forms.CharField(required=False) 
    actividades = forms.CharField(widget=forms.Textarea())
    class Meta:  
        model = DetalleProfesorCatedra         
        fields = ['nombre_profesor', 'apellido_profesor', 'profesor', 'categoria', 'situacion', 'dedicacion', 'tareas','actividades']
        exclude = ['planificacion']
        widgets = {
            'tareas': forms.CheckboxSelectMultiple(attrs={'class': 'multiple-select-list'}),
        }
        labels = {
            'profesor': _('Profesor'),
            'categoria': _('Categoría'),
            'situacion': _('Situación de Revista y/o Condición'),
            'dedicacion': _('Dedicación'),
            'tareas': _('Tareas/Funciones a realizar'),
        }
    def __init__(self, *args, **kwargs):
        asignatura_id = kwargs.pop('asignatura_id', None)
        planificacion_id = kwargs.pop('planificacion_id', None)
        super(DetalleProfesorCatedraForm, self).__init__(*args, **kwargs)
        asignatura = Asignatura.objects.get(id= asignatura_id)
        self.fields['profesor'].queryset = User.objects.filter(groups = Group.objects.get(name='profesor')).intersection(asignatura.profesor.all())
        self.fields['tareas'].queryset = TareasFunciones.objects.filter(planificacion_id = planificacion_id)
