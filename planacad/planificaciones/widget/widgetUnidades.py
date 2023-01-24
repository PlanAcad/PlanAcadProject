
from django import forms  
from django.urls import reverse

class CheckboxSelectMultipleWithPlaceholder(forms.CheckboxSelectMultiple):
    def __init__(self, attrs=None, choices=()):
        self.planificacion_id =  attrs.get('planificacion_id', None)
        super().__init__(attrs, choices)
        

    def render(self, name, value, attrs=None, renderer=None):
        if len(self.choices) > 1:
            return super().render(name, value, attrs, renderer)
        elif len(self.choices) == 1:
            if attrs is None:
                attrs = {}
            attrs["value"] = self.choices[0][0]
            label = 'Unidad ' + str(self.choices[0][1])
            checkbox = forms.CheckboxInput(attrs=attrs, check_test=lambda value: value in [value,])
            return checkbox.render(name, value) + ' ' + label
            ## tenes que guardar esta
        else:
            url = reverse('planificaciones:contenido',kwargs={'id_planificacion' : self.planificacion_id})
            return f'<input disabled /><a href="{url}" class="link-primary">Ir a sección 11: Contenido</a>'
            
