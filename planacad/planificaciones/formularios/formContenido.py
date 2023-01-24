from django import forms
from django.utils.translation import ugettext_lazy as _
from planificaciones.modelos.modelContenido import Contenido
from planificaciones.modelos.modelUnidad import Unidad



class ContenidoForm(forms.ModelForm):  
    objetivos = forms.CharField(widget=forms.Textarea())
    contenido = forms.CharField(widget=forms.Textarea())
    # unidad = forms.ModelChoiceField(
    #     queryset= Unidad.objects.filter(planificacion_id= kwargs.pop('planificacion_id'))
    #     ) 
    class Meta:  
        model = Contenido  
        exclude = ['planificacion']
        fields = "__all__"
       
    def __init__(self, *args, **kwargs):
        planificacion_id = kwargs.pop('planificacion_id')
        super(ContenidoForm, self).__init__(*args, **kwargs)
        self.fields['unidad'].queryset = Unidad.objects.filter(planificacion_id=planificacion_id)
