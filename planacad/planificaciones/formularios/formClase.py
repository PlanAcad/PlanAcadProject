from django import forms
from django.forms.widgets import DateInput
from planificaciones.modelos.modelClase import Clase

LUGARES = [
    ('Dentro del aula', 'Dentro del aula'),
    ('Fuera del aula', 'Fuera del aula')
]

MONTHS = {
    1: ('01'),
    2: ('02'),
    3: ('03'),
    4: ('04'),
    5: ('05'),
    6: ('06'),
    7: ('07'),
    8: ('08'),
    9: ('09'),
    10: ('10'),
    11: ('11'),
    12: ('12')
}

TIPO_EXAMEN = [
      ('P', 'Examen parcial'),
      ('R', 'Examen recuperatorio'),
      ('F', 'Examen final'),
      ('NA', 'No aplica')
]

class ClaseForm(forms.ModelForm):  
    lugar_desarrollo_de_clase = forms.ChoiceField(choices=LUGARES)
    es_examen = forms.CharField(widget=forms.RadioSelect(choices=TIPO_EXAMEN))

    def __init__(self, *args, **kwargs):
        super(ClaseForm, self).__init__(*args, **kwargs)
        #self.fields['fecha_clase'].widget = forms.SelectDateWidget(months=MONTHS, attrs={'class': 'form-fecha'})

    class Meta:  
        model = Clase
        fields = ['profesor_a_cargo','lugar_desarrollo_de_clase', 'fecha_clase', 'es_examen', 'unidad_tematica_o_tema', 'cantidad_tareas','resultado_de_aprendizaje']
        labels = {
            'profesor_a_cargo': 'Profesor a cargo de la clase',
            'lugar_desarrollo_de_clase': 'Lugar de desarrollo de la clase',
            'fecha_clase': 'Fecha de la clase',
            'es_examen': ' ',
            'unidad_tematica_o_tema': 'Unidad temática / tema',
            'cantidad_tareas': 'Cantidad de tareas por clase / semana',
            'resultado_de_aprendizaje': 'Resultado de aprendizaje',
        }
        widgets = {
            'profesor_a_cargo': forms.CheckboxSelectMultiple(attrs={'class': 'multiple-select-list'}),
            'unidad_tematica_o_tema': forms.CheckboxSelectMultiple(attrs={'class': 'multiple-select-list'}),
            'resultado_de_aprendizaje': forms.CheckboxSelectMultiple(attrs={'class': 'multiple-select-list'}),
            'fecha_examen': forms.DateInput(attrs={'class': 'date-picker'}),
        }
