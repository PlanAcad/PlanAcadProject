from django import forms
from django.utils.translation import ugettext_lazy as _
from planificaciones.modelos.modelContenido import Contenido
from planificaciones.modelos.modelUnidad import Unidad
from planificaciones.widget.widgetUnidades import CheckboxSelectMultipleWithPlaceholder
from django.db.models import Value
from django.db.models.functions import Concat
from django.db.models import CharField


class ContenidoForm(forms.ModelForm):  
    objetivos = forms.CharField(widget=forms.Textarea())
    contenido = forms.CharField(widget=forms.Textarea())
    class Meta:  
        model = Contenido  
        exclude = ['planificacion']
        fields = "__all__"
        
       
    def __init__(self, *args, **kwargs):
        planificacion_id = kwargs.pop('planificacion_id')
        super(ContenidoForm, self).__init__(*args, **kwargs)
        self.fields['unidad'].queryset = Unidad.objects.filter(planificacion_id=planificacion_id)

        # self.fields['unidad'].choices = Unidad.objects.filter(planificacion_id=planificacion_id)
        # self.fields['unidad'].widget = CheckboxSelectMultipleWithPlaceholder(attrs={'planificacion_id': planificacion_id,'class': 'multiple-select-list'},
                                                    # choices= list(Unidad.objects.filter(planificacion_id=planificacion_id)
                                                    # .annotate(title_number=Concat('numero', Value(': '), 'titulo',output_field=CharField())).values_list('id', 'title_number')
                                                    # .values_list('id','title_number')))

    def render(self):
        return self.as_table()
