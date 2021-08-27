from django import forms  
from planificaciones.modelos.modelSeccion1 import Seccion1

class Seccion1Form(forms.ModelForm):  
    cursado = forms.ChoiceField(choices=[
    ('A','Anual'),
    ('1','1er Cuatrimestre'),
    ('2','2do Cuatrimestre')
    ], widget=forms.RadioSelect())
    class Meta:  
        model = Seccion1  
        exclude = ['carrera', 'asignatura']        