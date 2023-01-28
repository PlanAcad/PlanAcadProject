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
            #  'unidad_tematica': forms.CheckboxSelectMultiple(attrs={'class': 'multiple-select-list'}),
            # 'resultados_de_aprendizaje': forms.CheckboxSelectMultiple(attrs={'class': 'multiple-select-list'})
        }

    def __init__(self, *args, **kwargs):
        planificacion_id = kwargs.pop('planificacion_id')
        super(ActividadForm, self).__init__(*args, **kwargs)
        self.fields['unidad_tematica'].queryset = Unidad.objects.filter(planificacion_id=planificacion_id)
        self.fields['unidad_tematica'].choices = Unidad.objects.filter(planificacion_id=planificacion_id)
        self.fields['unidad_tematica'].widget = CheckboxSelectMultipleWithPlaceholder(attrs={'planificacion_id': planificacion_id,'class': 'multiple-select-list'},
                                                    choices= list(Unidad.objects.filter(planificacion_id=planificacion_id)
                                                    .annotate(title_number=Concat('numero', Value(': '), 'titulo',output_field=CharField())).values_list('id', 'title_number')
                                                    .values_list('id','title_number')))
        self.fields['resultados_de_aprendizaje'].queryset = ResultadoDeAprendizaje.objects.filter(planificacion_id = planificacion_id)
        self.fields['resultados_de_aprendizaje'].choices = ResultadoDeAprendizaje.objects.filter(planificacion_id=planificacion_id)
        self.fields['resultados_de_aprendizaje'].widget = CheckboxSelectMultipleResultadoDeAprendizaje(attrs={'planificacion_id': planificacion_id,'class': 'multiple-select-list'},
                                                    choices= list(ResultadoDeAprendizaje.objects.filter(planificacion_id=planificacion_id)
                                                    .values_list('id', 'resultado')))
        

    def render(self):
        return self.as_table()
        
       


