from django import forms  
from django.forms import ModelForm
from planificaciones.modelos.modelActividad import Actividad
from planificaciones.modelos.modelUnidad import Unidad
from planificaciones.modelos.modelResultadoAprendizaje import ResultadoDeAprendizaje

from django.db.models import Value
from django.db.models.functions import Concat
from django.db.models import CharField
from planificaciones.widget.widgetUnidades import CheckboxSelectMultipleWithPlaceholder
from planificaciones.widget.widgetResultadoDeAprendizaje import CheckboxSelectMultipleResultadoDeAprendizaje


class ActividadForm(ModelForm):
    
    class Meta:
        model = Actividad
        fields = ['actividad', 'unidad_tematica', 'lugar', 'indicadores_de_logro', 'tecnicas_de_evaluacion', 'tipo_de_evaluacion', 'resultados_de_aprendizaje']
        widgets = {
             'unidad_tematica': forms.CheckboxSelectMultiple(attrs={'class': 'multiple-select-list'}),
             'resultados_de_aprendizaje': forms.CheckboxSelectMultiple(attrs={'class': 'multiple-select-list'})
        }

        
       


