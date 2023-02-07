from django import forms  
from planificaciones.modelos.modelAsignatura import Asignatura
from django.contrib.auth.models import User, Group
from django.utils.translation import gettext_lazy as _


class AsignaturaMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return "{} del {} año, comision {}".format(obj.nombre_materia, obj.ano, obj.comision)

class AsignaturaCarreraForm(forms.Form):
    asignaturas = AsignaturaMultipleChoiceField(
        queryset=None,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'multiple-select-list'})
    )
    comentario = forms.CharField(
        max_length=500, 
        widget=forms.Textarea()
        )