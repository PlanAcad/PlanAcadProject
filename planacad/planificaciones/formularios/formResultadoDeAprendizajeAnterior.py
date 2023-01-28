from django import forms  
from planificaciones.modelos.modelResultadoDeAprendizajeAnterior import ResultadoDeAprendizajeAnterior
from planificaciones.modelos.modelResultadoAprendizaje import ResultadoDeAprendizaje
from planificaciones.modelos.modelAsignatura import Asignatura
from planificaciones.modelos.modelPlanificacion import Planificacion



class ResultadoDeAprendizajeAnteriorForm(forms.ModelForm):

    class Meta:  
        model = ResultadoDeAprendizajeAnterior
        exclude = ['planificacion']
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        planificacion_id = kwargs.pop('planificacion_id')
        super(ResultadoDeAprendizajeAnteriorForm, self).__init__(*args, **kwargs)
        planificacion = Planificacion.objects.get(id = planificacion_id)
        self.fields['asignatura'].queryset = Asignatura.objects.filter(planificacion__estado='A').distinct().exclude(id = planificacion.asignatura_id)
        
        
  