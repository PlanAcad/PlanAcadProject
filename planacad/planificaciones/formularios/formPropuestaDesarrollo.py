from django import forms  
from planificaciones.modelos.modelPropuestaDesarrollo import PropuestaDesarrollo

class PropuestaDesarrolloForm(forms.ModelForm):  

    class Meta:  
        model = PropuestaDesarrollo  
        exclude = ['planificacion']
        widgets = {
            'subcompetencias': forms.CheckboxSelectMultiple(attrs={'class': 'multiple-select-list'}),
            'resultados_de_aprendizaje': forms.CheckboxSelectMultiple(attrs={'class': 'multiple-select-list'}),
            'unidades': forms.CheckboxSelectMultiple(attrs={'class': 'multiple-select-list'}),
            'bibliografias': forms.CheckboxSelectMultiple(attrs={'class': 'multiple-select-list'}),
            'estrategias_ens': forms.CheckboxSelectMultiple(attrs={'class': 'multiple-select-list'}),
        }