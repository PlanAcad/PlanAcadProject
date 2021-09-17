from django.forms import ModelForm
from planificaciones.modelos.modelActividad import Actividad

class ActividadForm(ModelForm):
    class Meta:
        model = Actividad
        fields = ['actividad', 'unidad_tematica', 'lugar', 'indicadores_de_logro', 'tecnicas_de_evaluacion', 'tipo_de_evaluacion', 'resultados_de_aprendizaje']
