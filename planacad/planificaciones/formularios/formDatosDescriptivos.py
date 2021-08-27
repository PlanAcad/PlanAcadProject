from django import forms  
from planificaciones.modelos.modelDatosDescriptivos import DatosDescriptivos

class DatosDescriptivosForm(forms.ModelForm):  
    cursado = forms.ChoiceField(choices=[
    ('A','Anual'),
    ('1','1er Cuatrimestre'),
    ('2','2do Cuatrimestre')
    ], widget=forms.RadioSelect())
    class Meta:  
        model = DatosDescriptivos  
        exclude = ['carrera', 'asignatura']        