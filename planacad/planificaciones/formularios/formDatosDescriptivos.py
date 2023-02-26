from django import forms  
from django.utils.translation import gettext_lazy as _
from planificaciones.modelos.modelDatosDescriptivos import DatosDescriptivos
from planificaciones.modelos.modelDiasCursado import DiasCursado

class DatosDescriptivosForm(forms.ModelForm):  
    cursado = forms.ChoiceField(choices=[
    ('A','Anual'),
    ('1','1er Cuatrimestre'),
    ('2','2do Cuatrimestre')
    ], widget=forms.RadioSelect())
    dias = forms.ModelMultipleChoiceField(
            queryset=DiasCursado.objects.all(),
            widget=forms.CheckboxSelectMultiple()) 
    class Meta:  
        model = DatosDescriptivos  
        exclude = ['carrera', 'asignatura']        
        labels = {
            'institucion': _('Institución'),
            'area_bloque': _('Área / Bloque'),
            'porcentaje_horas_en_area': _('Porcentaje de horas cátedra de la asignatura en el área'),
            'porcentaje_horas_en_bloque': _('Porcentaje de horas cátedra de la asignatura en el bloque'),
        }