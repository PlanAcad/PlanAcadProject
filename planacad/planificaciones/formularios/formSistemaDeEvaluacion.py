from django import forms  
from django.forms import ModelForm
from planificaciones.modelos.modelActividad import Actividad
from planificaciones.modelos.modelUnidad import Unidad
from planificaciones.modelos.modelResultadoAprendizaje import ResultadoDeAprendizaje

from django.db.models import Value
from django.db.models.functions import Concat
from django.db.models import CharField


class ActividadForm(ModelForm):
    indicadores_de_logro = forms.CharField(widget=forms.Textarea()) 
    tecnicas_de_evaluacion = forms.CharField(widget=forms.Textarea())
    class Meta:
        model = Actividad
        fields = ['actividad', 'unidad_tematica', 'lugar', 'indicadores_de_logro', 'tecnicas_de_evaluacion', 'tipo_de_evaluacion', 'resultados_de_aprendizaje']
        widgets = {
             'unidad_tematica': forms.CheckboxSelectMultiple(attrs={'class': 'multiple-select-list'}),
             'resultados_de_aprendizaje': forms.CheckboxSelectMultiple(attrs={'class': 'multiple-select-list'})
        }

        
       


