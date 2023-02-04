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