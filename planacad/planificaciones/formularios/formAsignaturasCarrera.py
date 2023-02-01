from django import forms  
from planificaciones.modelos.modelAsignatura import Asignatura
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext_lazy as _


class AsignaturaMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return "{} del {} año, comision {}".format(obj.nombre_materia, obj.ano, obj.comision)

class AsignaturaCarreraForm(forms.Form):
    def __init__(self, carrera, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['asignaturas'].queryset = Asignatura.objects.filter(carrera=carrera)
    
    asignaturas = AsignaturaMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'multiple-select-list'})
    )
    comentario = forms.CharField(
        max_length=500, 
        widget=forms.Textarea()
        )